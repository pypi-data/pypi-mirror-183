from dataclasses import dataclass
from enum import Enum
from typing import List

from qm.pb.job_results_pb2 import GetJobErrorsRequest, GetJobErrorsResponse
from qm.pb.job_results_pb2_grpc import JobResultsServiceStub


class ExecutionErrorSeverity(Enum):
    Warn = 0
    Error = 1


@dataclass(frozen=True)
class ExecutionError:
    error_code: int
    message: str
    severity: ExecutionErrorSeverity

    def __repr__(self):
        return f"{self.error_code}\t\t{self.severity.name}\t\t{self.message}"


class ExecutionReport:
    def __init__(self, job_id: str, service: JobResultsServiceStub) -> None:
        super().__init__()
        self._errors: List[ExecutionError] = []
        self._job_id: str = job_id
        self._service: JobResultsServiceStub = service
        self._errors = ExecutionReport._load_errors(self._job_id, self._service)

    @staticmethod
    def _load_errors(
        job_id: str, service: JobResultsServiceStub
    ) -> List[ExecutionError]:
        request = GetJobErrorsRequest()
        request.jobId = job_id
        response: GetJobErrorsResponse = service.GetJobErrors(request)
        return [
            ExecutionError(
                error_code=item.errorCode,
                message=item.message,
                severity=ExecutionReport._parse_error_severity(item.errorSeverity),
            )
            for item in response.errors
        ]

    @staticmethod
    def _parse_error_severity(error_severity) -> ExecutionErrorSeverity:
        if error_severity == GetJobErrorsResponse.WARNING:
            return ExecutionErrorSeverity.Warn
        elif error_severity == GetJobErrorsResponse.ERROR:
            return ExecutionErrorSeverity.Error

    def has_errors(self) -> bool:
        """
        :return: True if encountered a runtime error while executing the job.
        """
        return len(self._errors) > 0

    def errors(self) -> List[ExecutionError]:
        """

        :return: list of all execution errors for this job
        """
        return self._errors.copy()

    def _report_header(self) -> str:
        return (
            f"Execution report for job {self._job_id}\nErrors:\n"
            f"Please refer to section: Error Indications and Error Reporting in documentation for additional information\n\n"
            "code\t\tseverity\tmessage"
        )

    def __repr__(self) -> str:
        if self.has_errors():
            errorsStr = ""
            for error in self._errors:
                errorsStr += "\n" + str(error)
            return self._report_header() + errorsStr
        else:
            return f"Execution report for job {self._job_id}\nNo errors"
