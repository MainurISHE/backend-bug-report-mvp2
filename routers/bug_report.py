from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import SessionLocal

from app.database.models import BugReport

from app.schemas.bug_report import BugReportSchema

router = APIRouter(
    prefix="/bug-report",
    tags=["Bug Report"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_bug_report(
    data: BugReportSchema,
    db: Session = Depends(get_db)
):
    bug = BugReport(
        email=data.email,
        author=data.author,
        release_build=data.release_build,
        fixed_by=data.fixed_by,
        description=data.description,
        priority=data.priority,
        severity=data.severity
    )

    db.add(bug)

    db.commit()

    db.refresh(bug)

    return {
        "message": "Bug report created",
        "id": bug.id
    }