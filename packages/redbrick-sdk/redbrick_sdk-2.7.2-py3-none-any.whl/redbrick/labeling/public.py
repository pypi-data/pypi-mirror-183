"""Public interface to labeling module."""
import os
import json
import asyncio
from typing import List, Dict, Optional
from copy import deepcopy
from functools import partial

import aiohttp
import tqdm  # type: ignore

from redbrick.common.context import RBContext
from redbrick.common.constants import MAX_CONCURRENCY
from redbrick.utils.logging import log_error
from redbrick.utils.pagination import PaginationIterator
from redbrick.utils.async_utils import gather_with_concurrency
from redbrick.utils.rb_label_utils import clean_rb_label
from redbrick.utils.files import NIFTI_FILE_TYPES, upload_files


class Labeling:
    r"""
    Perform programmatic labeling and review tasks.

    The Labeling class allows you to programmatically submit tasks.
    This can be useful for times when you want to make bulk actions
    e.g accepting several tasks, or make automated actions like using automated
    methods for review.

    .. admonition:: Information

      The Labeling module provides several methods to query tasks and assign tasks to
      different users. Refer to this section for guidance on when to use each method:

      - :obj:`assign_task`.
        Use this method when you already have
        the ``task_id`` you want to assign to a particular user. If you don't have the
        ``task_id``, you can query all the tasks using :obj:`~redbrick.export.Export.export_tasks`
        or query tasks assigned to a particular user/unassigned tasks using :obj:`get_task_queue`.

      - :obj:`get_task_queue`.
        Use this method when you want to retrieve the tasks assigned to a particular user, or
        you want to fetch all the unassigned tasks in your project. This can be useful in
        preparation for using :obj:`assign_task` to programmatically assigning tasks,
        or :obj:`put_tasks` to programmatically label/review tasks assigned to you.

      - :obj:`get_tasks`.
        Use this method to fetch all tasks `already assigned to the current API Key`.
        This can be useful in preparation for re-assigned those tasks to another
        user (through :obj:`assign_task`) or for programmatically submitting them
        through :obj:`put_tasks`.

    """

    def __init__(
        self,
        context: RBContext,
        org_id: str,
        project_id: str,
        review: bool = False,
    ) -> None:
        """Construct Labeling."""
        self.context = context
        self.org_id = org_id
        self.project_id = project_id
        self.review = review

    def get_tasks(self, stage_name: str, count: int = 1) -> List[Dict]:
        """
        Get tasks assigned to the API Key.

        Get a list of tasks from ``stage_name`` for the current API Key to work upon. If
        the current API Key is not assigned any tasks, calling this method will automatically
        assign tasks to the API Key.

        >>> project = redbrick.get_project(...)
        >>> label_tasks = project.labeling.get_tasks(...)
        >>> review_tasks = project.review.get_tasks...)

        Parameters
        -------------
        stage_name: str
            The name of the stage your want to get tasks from. You can
            find the stage name on the workflow overview on the project
            dashboard.

        count: int = 1
            The number of tasks to retrieve. We recommend keeping this
            < 50.

        Returns
        ----------
        List[Dict]
            Tasks that are queued in this stage. Please see reference doc
            for formats.
            https://docs.redbrickai.com/python-sdk/reference#task-objects
        """
        tasks = self.context.labeling.get_labeling_tasks(
            self.org_id, self.project_id, stage_name, count=count
        )

        def _clean_tasks(task: Dict) -> Dict:
            task_id = task["taskId"]
            labels = json.loads(task.get("taskData", {}).get("labelsData", "[]"))
            labels_cleaned = [clean_rb_label(label) for label in labels]

            items = task["datapoint"]["items"]
            items_presigned = task["datapoint"]["itemsPresigned"]
            name = task["datapoint"]["name"]

            return {
                "taskId": task_id,
                "labels": labels_cleaned,
                "items": items,
                "itemsPresigned": items_presigned,
                "name": name,
            }

        return [_clean_tasks(task) for task in tasks]

    async def _put_task(
        self, session: aiohttp.ClientSession, stage_name: str, task: Dict
    ) -> Optional[Dict]:
        task_id = task["taskId"]
        try:
            if self.review:
                review_val = task["reviewVal"]
                await self.context.labeling.put_review_task_result(
                    session,
                    self.org_id,
                    self.project_id,
                    stage_name,
                    task_id,
                    review_val,
                )
            else:
                labels_path: Optional[str] = None
                if (
                    task.get("labelsPath")
                    and (
                        str(task["labelsPath"]).endswith(".nii")
                        or str(task["labelsPath"]).endswith(".nii.gz")
                    )
                    and os.path.isfile(task["labelsPath"])
                ):
                    file_type = NIFTI_FILE_TYPES["nii"]
                    presigned = await self.context.labeling.presign_labels_path(
                        session, self.org_id, self.project_id, task_id, file_type
                    )
                    if (
                        await upload_files(
                            [
                                (
                                    task["labelsPath"],
                                    presigned["presignedUrl"],
                                    file_type,
                                )
                            ],
                            "Uploading labels",
                            False,
                        )
                    )[0]:
                        labels_path = presigned["filePath"]

                await self.context.labeling.put_labeling_results(
                    session,
                    self.org_id,
                    self.project_id,
                    stage_name,
                    task_id,
                    json.dumps(task["labels"], separators=(",", ":")),
                    labels_path,
                    not bool(task.get("draft")),
                )

        except ValueError as error:
            log_error(error)
            point_error = deepcopy(task)
            point_error["error"] = error
            return point_error
        return None

    async def _put_tasks(self, stage_name: str, tasks: List[Dict]) -> List[Dict]:
        conn = aiohttp.TCPConnector(limit=MAX_CONCURRENCY)
        async with aiohttp.ClientSession(connector=conn) as session:
            coros = [self._put_task(session, stage_name, task) for task in tasks]
            temp = await gather_with_concurrency(10, coros, "Uploading tasks")
        await asyncio.sleep(0.250)  # give time to close ssl connections
        return [val for val in temp if val]

    def put_tasks(self, stage_name: str, tasks: List[Dict]) -> List[Dict]:
        """
        Put tasks with new labels or a review result.

        Use this method to programmatically add labels to tasks in `Label stage`,
        or to programmatically accept/reject tasks in a `Review stage`. If you don't already
        have a list of ``task_id``, you can use :obj:`~redbrick.export.Export.export_tasks` to
        get a list of all tasks in your project, or you can use :obj:`get_tasks`
        to get a list of tasks assigned to you.

        .. admonition:: Assign tasks to your API key
            :class: caution

            You must assign tasks to your API Key `before` you use :obj:`put_tasks`. You cannot
            programmatically label/review tasks that are not assigned to you (in this case, your
            API key).

        .. tab:: Label

            .. code:: python

                project = redbrick.get_project(...)
                tasks = [
                    {
                        "task_id": "...",
                        "labels": [{...}]
                    },
                ]
                project.labeling.put_tasks(stage_name="Label", tasks=tasks)


        .. tab:: Review

            .. code:: python

                project = redbrick.get_project(...)
                tasks = [
                    {
                        "task_id": "...",

                        # Set reviewVal to True if you want to accept the task
                        "reviewVal": True
                    },
                    {
                        "task_id": "...",

                        # Set reviewVal to False if you want to reject the task
                        "reviewVal": False
                    }
                ]
                project.review.put_tasks(stage_name="Review_1", tasks=tasks)


        Parameters
        --------------
        stage_name: str
            The stage to which you want to submit the tasks. This must be the
            same stage as which you called get_tasks on.

        tasks: List[Dict]
            Tasks with new labels or review result.

        Returns
        ---------------
        List[Dict]
            A list of tasks that failed the upload.
        """
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self._put_tasks(stage_name, tasks))

    def assign_task(
        self,
        stage_name: str,
        task_id: str,
        email: Optional[str] = None,
        current_user: bool = False,
        refresh: bool = False,
    ) -> None:
        """
        Assign tasks to specified email or current API key.

        You must specify either the user ``email`` or set ``current_user`` to ``True``.

        >>> project = redbrick.get_project(org_id, project_id, api_key)
        >>> project.labeling.assign_task(stage_name, task_id, email)

        Parameters
        ------------------
        stage_name: str
            The stage name within which the task currently is. If you want to assign
            ``task_id`` in the ``Label`` stage, set ``stage_name="Label"``.

        task_id: str
            The unique ``task_id`` of the task you want to assign.

        email: Optional[str] = None
            The email of the user you want to assign this task to. Make sure the
            user has adequate permissions to be assigned this task in the project.

        current_user: bool = False
            If true, will assign the task to the API KEY being used with the SDK.

        refresh: bool = False
            Used for projects with Consensus activated. If `True`, will `overwrite` the assignment
            to the current users.
        """
        self.context.labeling.assign_tasks(
            self.org_id,
            self.project_id,
            stage_name,
            [task_id],
            [email] if email else None,
            current_user,
            refresh,
        )

    def get_task_queue(
        self,
        stage_name: str,
        concurrency: int = 50,
        user_id: Optional[str] = None,
        fetch_unassigned: bool = True,
    ) -> List[Dict]:
        """Get all tasks in queue.

        Returns all the tasks assigned to a particular user and/or
        tasks that are unassigned.

        Parameters
        --------------
        stage_name: str
            The stage for which you want to query the task queue.

        concurrency: int = 50
            The number of tasks to retrieve at a time.
            We recommend keeping this <= 50.

        user_id: Optional[str] = None
            The user id for which you want to query the task queue.
            If None, will query for current API Key.

        fetch_unassigned: bool = True
            Whether to fetch unassigned tasks.

        Returns
        ---------------
        List[Dict]
            List of tasks in queue - [{"taskId", "name", "createdAt"}]
        """
        if not user_id:
            user_id = self.context.key_id

        my_iter = PaginationIterator(
            partial(
                self.context.export.task_search,
                self.org_id,
                self.project_id,
                stage_name,
                None,
                {"userId": user_id},
                concurrency,
            )
        )

        with tqdm.tqdm(
            my_iter, unit=" datapoints", desc="Fetching assigned tasks"
        ) as progress:
            datapoints = [
                {
                    "taskId": task["taskId"],
                    "name": task["datapoint"]["name"],
                    "assignedTo": (
                        (task["currentStageSubTask"] or {}).get("assignedTo") or {}
                    ).get("email"),
                    "status": (task["currentStageSubTask"] or {}).get("state"),
                    "items": task["datapoint"]["items"],
                    "itemsPresigned": task["datapoint"]["itemsPresigned"],
                    "createdAt": task["createdAt"],
                }
                for task in progress
            ]

        if fetch_unassigned:
            my_iter = PaginationIterator(
                partial(
                    self.context.export.task_search,
                    self.org_id,
                    self.project_id,
                    stage_name,
                    None,
                    {"userId": None},
                    concurrency,
                )
            )

            with tqdm.tqdm(
                my_iter, unit=" datapoints", desc="Fetching unassigned tasks"
            ) as progress:
                datapoints += [
                    {
                        "taskId": task["taskId"],
                        "name": task["datapoint"]["name"],
                        "assignedTo": None,
                        "status": (task["currentStageSubTask"] or {}).get("state"),
                        "items": task["datapoint"]["items"],
                        "itemsPresigned": task["datapoint"]["itemsPresigned"],
                        "createdAt": task["createdAt"],
                    }
                    for task in progress
                ]

        return datapoints

    async def _tasks_to_start(self, task_ids: List[str]) -> None:
        conn = aiohttp.TCPConnector(limit=MAX_CONCURRENCY)
        async with aiohttp.ClientSession(connector=conn) as session:
            coros = [
                self.context.labeling.move_task_to_start(
                    session, self.org_id, self.project_id, task_id
                )
                for task_id in task_ids
            ]
            await gather_with_concurrency(10, coros, "Moving tasks to Start")
        await asyncio.sleep(0.250)  # give time to close ssl connections

    def move_tasks_to_start(self, task_ids: List[str]) -> None:
        """Move groundtruth tasks back to start."""
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self._tasks_to_start(task_ids))
