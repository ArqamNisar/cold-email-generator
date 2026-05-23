from pydantic import BaseModel
from typing import Optional


class Lead(BaseModel):
    name: str
    title: str
    company: str
    linkedin_url: Optional[str]
    email: Optional[str]
    apollo_id: str