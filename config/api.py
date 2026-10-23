from typing import List
from ninja import NinjaAPI, Schema, Field
from ninja.errors import HttpError
from course.models import Course 

api = NinjaAPI()

class CourseIn(Schema):
    title: str
    duration: int = Field(..., gt=0)
    teacher: str


class CourseOut(Schema):
    id: int
    title: str
    duration: int = Field(..., gt=0)
    teacher: str


@api.post("/course")
def create_course(request, data: CourseIn):
    course = Course.objects.create(**data.model_dump())
    return{"message": f"Курс {course.title} добавлен"}

@api.get("/course", response=List[CourseOut])
def get_course(request):
    return Course.objects.all()

@api.put("/course/{course_id}")
def updata_course(request, course_id: int, data: CourseIn):
    course = Course.objects.filter(id=course_id).first()
    if not course:
        raise HttpError(322, "курса нет")
    course.title = data.title
    course.duration = data.duration
    course.teacher = data.teacher
    course.save()
    return {"message": f"Курс {course.title} обновлен"}

@api.delete("/course/{course_id}")
def delete_course(request, course_id: int):
    course = Course.objects.filter(id=course_id).first()
    if not course:
        raise HttpError(322, "курса нет")
    course.delete()
    return{"message": "Курс удален"}