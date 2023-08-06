"""
Workflows Client
"""
from relevanceai.utils.base import _Base
from enum import Enum
from typing import Union


class WorkflowStatus(Enum):
    IN_PROGRESS: str = "inprogress"
    COMPLETED: str = "complete"
    FAILED: str = "failed"


class WorkflowsClient(_Base):
    def __init__(self, credentials):
        super().__init__(credentials)

    def trigger(
        self,
        params: dict,
        notebook_path: str,
        instance_type: str,
        dataset_id: str,
        send_email: bool = True,
    ):
        """
        Trigger a workflow
        """
        return self.make_http_request(
            "/workflows/trigger",
            method="POST",
            parameters={
                "params": params,
                "notebook_path": notebook_path,
                "instance_type": instance_type,
                "dataset_id": dataset_id,
                "send_email": send_email,
            },
        )

    def list(self):
        return self.make_http_request(
            "/workflows/list",
            method="GET",
        )

    def get(self, workflow_id: str):
        """
        Returns

            {
                "job_status": "InProgress",
                "job_message": "string",
                "creation_time": "string",
                "notebook_path": "string",
                "params": { },
                "_id": "string",
                "metadata": { }
            }
        """
        return self.make_http_request(f"/workflows/{workflow_id}/get", method="POST")

    def metadata(self, workflow_id: str, metadata: dict):
        """
        Update metadata for a workflow run
        """
        return self.make_http_request(
            f"/workflows/{workflow_id}/metadata",
            method="POST",
            parameters={"metadata": metadata},
        )

    def status(
        self,
        workflow_id: str,
        workflow_name: str,
        metadata: dict=None,
        additional_information: str = "",
        status: Union[WorkflowStatus, str] = WorkflowStatus.IN_PROGRESS,
        send_email: bool = True,
    ):
        """
        If status is complete, it triggers an email.
        """
        if isinstance(status, WorkflowStatus):
            status = status.value
        if metadata is None:
            metadata = {}
        return self.make_http_request(
            f"/workflows/{workflow_id}/status",
            method="POST",
            parameters={
                "status": status,
                "workflow_name": workflow_name,
                "additional_information": additional_information,
                "metadata": metadata,
                "send_email": send_email,
            },
        )
