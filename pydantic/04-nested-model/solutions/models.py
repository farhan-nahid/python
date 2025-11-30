from pydantic import BaseModel
from typing import List, Optional

class Course(BaseModel):
  id: int
  name: str
  modules: List[Module]
  
  
class Module(BaseModel):
  id: int
  name: int
  course: Course
  lessons: Optional[List[Lesson]] = None


class Lesson(BaseModel):
  id: int
  name: str
  topic: str
  module: Module
  course: Course
