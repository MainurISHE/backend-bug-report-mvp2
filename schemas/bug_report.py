from pydantic import BaseModel


class BugReportSchema(BaseModel):
    email: str
    author: str
    release_build: str
    fixed_by: str
    description: str
    priority: str
    severity: str