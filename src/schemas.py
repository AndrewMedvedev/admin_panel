from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class EventSchema(BaseModel):
    name_event: str
    date_time: datetime
    location: str
    description: str
    points_for_the_event: float | None = None
    limit_people: int | None = None

    def to_dict(self) -> dict[str, str | float]:
        result: dict[str, str | float] = {
            "name_event": self.name_event,
            "date_time": self.date_time.isoformat(),
            "location": self.location,
            "description": self.description,
        }
        if self.points_for_the_event is not None:
            result["points_for_the_event"] = self.points_for_the_event
        if self.limit_people is not None:
            result["limit_people"] = self.limit_people

        return result
