from datetime import datetime
from pydantic import BaseModel, field_validator


class AddEventSchema(BaseModel):

    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: int | None
    limit_people: int | None


    @field_validator("date_time")
    @classmethod
    def validate_datetime(cls, v: datetime) -> dict:
        return v.isoformat()
    
