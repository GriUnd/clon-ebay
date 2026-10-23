from typing import List
from ninja import NinjaAPI, Schema, Field
from ninja.errors import HttpError
from teacher.models import Teacher
from django.shortcuts import get_object_or_404

api = NinjaAPI()

# @api.get("/")
# def read_root(request):
#     return {"message": "Grigory"}

# @api.get("/about")
# def about(request):
#     return {
#         "username": "system42",
#         "email": "system42@example.com",
#         "is_active": True,
#         "roles": ["developer", "admin"]
#     }

# @api.get("/hello/{name}")
# def say_hello(request, name: str):
#     return {"message": f"hello, {name}!"}

# @api.get("/sum")
# def get_sum(request, a: int, b: int):
#     result = a + b
#     return {"a": a, "b": b, "sum": result}

# @api.get("/users/{user_id}")
# def get_user_info(request, user_id: int, active: bool = True):
#     return {"user_id": user_id, "active": active}

# @api.get("/square/{number}")
# def get_square_numbers(request, number: int,):
#     number ** 2
#     return {"number": number, "square": number ** 2}

# @api.get("/greet")
# def user_name_age(request, name: str, age: int):
#     return {"message": f"hello, {name}! you {age} age."}

# @api.get("/compare")
# def more_numb(request, a: int, b: int):
#     if a > b:
#         return{"message":f"{a} more {b}"}
#     else:
#         return{"message":f"{a} less {b}"}

# class FeedbackSchema(Schema):
#     name: str
#     text: str

# @api.post("/Feedback")
# def Feedback(request, user_review: FeedbackSchema):
#     if user_review.text != "":
#         return{"message": f"Спасибо за отзыв, {user_review.name}!"}
#     else:
#         return{"error": "Отзыв не может быть пустым"}


# class calcSchema(Schema):
#     a: int
#     b: int

# @api.post("/calc")
# def calc(request, data: calcSchema):
#     a = data.a
#     b = data.b
#     if b == 0:
#         return{"error":f"деление на {b} невозможно"}
#     else:
#         return{"message":f"sum: {a + b}, sub: {a - b}, mul: {a * b}, div: {a / b}"}

# movie_bd = [
#     {"id": 1, "title": "Интерстеллар", "year": 2014, "rating": 8.6}
# ]

# class MovieSchema(Schema):
#     id: int
#     title: str
#     year: int
#     rating: float

# @api.get("/movie")
# def list_movie(request):
#      return movie_bd

# @api.get("/movie/{movie_id}")
# def list_id(request, movie_id: int):
#     for movie in movie_bd:
#         if movie["id"] == movie_id:
#             return movie

# @api.post("/movieadd")
# def add_movie(request, data: MovieSchema):
#     movie_db.append(data.dict())
#     return{"message": f"Фильм {data.title} добавлен!"}

# book_bd = [
#     {"id": 1, "title": "Война и мир", "author": "Толстой", "year": 1869}
# ]

# class BookSchema(Schema):
#     id: int
#     title: str
#     author: str
#     year: int

# @api.post("/bookadd")
# def add_book(request, data: BookSchema):
#     book_bd.append(data.dict())
#     return{"message": f"Книга {data.title} добальна!"}

# @api.get("/book")
# def list_book(request):
#     return book_bd

# @api.get("/book/{author}")
# def list_author(request, author: str):
#     author_books = [book for book in book_bd if book["author"].lower() == author.lower()]
#     return author_books

# shop_bd = [
#     {"id": 1, "name": "Книга", "price": 20.5},
#     {"id": 3, "name": "Игрушка", "price": 45.0}
# ]

# class ShopSchema(Schema):
#     id: int
#     name: str
#     price: float

# @api.post("/products")
# def shop_add(request, data: ShopSchema):
#     shop_bd.append(data.dict())
#     return{"message": f"Товар {data.name} добавлен"}

# @api.get("/products")
# def list_shop(request):
#     return shop_bd

# @api.put("/products/{id}")
# def change_price(request, id: int, update_price: ShopSchema):
#     for i, item in enumerate(shop_bd):
#         if item["id"] == id:
#             shop_bd[i] = update_price.dict() 
#             return {"message": "Цены обновлены"}
#     raise HttpError(404, "Продукт не найден")

        
# @api.get("/products/search")
# def search_shop_price(request, min_price: float, max_price: float):
#     filtered_products = [
#         product for product in shop_bd 
#         if min_price <= product["price"] <= max_price
#     ]
#     return filtered_products

# @api.delete("/products/{id}")
# def delete_products(request, id: int,):
#     for i, item in enumerate(shop_bd):
#         if item["id"] == id:
#             shop_bd.remove(item)
#             return {"message": "Продукт удален"}
#     raise HttpError(404, "Продукт не найден")

# student_bd = [
#     {"id": 1, "name": "Иван", "group": "Р-153", "average_score": 3.8},
#     {"id": 2, "name": "Никита", "group": "ИЛ-256", "average_score": 4.3}
# ]

# class Student_list(Schema):
#     id: int
#     name: str
#     group: str
#     average_score: float

# @api.get("/students")
# def list_student(request):
#     return student_bd

# @api.post("/students")
# def add_student(request, data: Student_list):
#     student_bd.append(data.dict())
#     return {"message": f"Студент {data.name} добавлен"}
# @api.put("/students/{id}")
# def change_price(request, id: int, update_average_score: Student_list):
#     for i, item in enumerate(student_bd):
#         if item["id"] == id:
#             student_bd[i] = update_average_score.dict() 
#             return {"message": "Средний балл обновлен"}
#     raise HttpError(404, "Студент не найден")

# library_bd = [
#     {"id": 1, "title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1967, "available": True},
#     {"id": 2, "title": "1844", "author": "Джордж Оруэлл", "year": 1949, "available": False},
#     {"id": 3, "title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "available": True}
# ]

# class librarySchema(Schema):
#     id: int
#     title: str
#     author: str
#     year: int
#     available: bool

# @api.get("/library")
# def list_library(request):
#     return library_bd

# @api.post("/library")
# def add_library(request, data: librarySchema):
#     book_id = data.id
#     for i, book in enumerate(library_bd):
#         if book["id"] == book_id:
#             raise HttpError(400, "Такая книга есть")
#     library_bd.append(data.dict())
#     return{"message": f"книга {data.title} добавленна"}
        
        
        
# @api.put("/library/{id}")
# def change_book(request, id: int, update_book: librarySchema):
#     for i, book in enumerate(library_bd):
#         if book["id"] == id:
#             library_bd[i] = update_book.dict()
#             return{"message": "каталог книг обновлен"}
#     raise HttpError(404, "книга не найдена")

# @api.delete("/library/{id}")
# def delete_book(request, id: int):
#     for i, book in enumerate(library_bd):
#         if book["id"] == id:
#             library_bd.remove(book)
#             return{"message": "книга удаленна"}
#     raise HttpError(404, "книга не найдена")

# posts = [
#     {"id": 1, "title": "Обновлённый пост", "content": "Исправленный текст", "author": "Анна"}
# ]
# class instaposts(Schema):
#     id: int
#     title: str
#     content: str
#     author: str

# @api.post("/posts")
# def create_posts(request, data: instaposts):
#     # Проверяем на дубликат ID
#     for post in posts:
#         if post["id"] == data.id:
#             raise HttpError(400, "Пост с таким ID уже существует")
#     posts.append(data.dict())
#     return {"message": "пост создан"}

# @api.get("/posts")
# def list_posts(request):
#     return posts

# @api.put("/posts/{id}")
# def change_posts(request, id: int, update_posts: instaposts):
#     for i, post in enumerate(posts):
#         if post["id"] == id:
#             post["title"] = update_posts.title
#             post["content"] = update_posts.content
#             return{"message": "Пост обновлён!"}
#     raise HttpError(400, "Такого поста нету")

# @api.delete("/posts/{id}")
# def delete_posts(request, id: int):
#     for post in posts:
#         if post["id"] == id:
#             posts.remove(post)
#             return {"message": "Пост удален!"}
            
#     raise HttpError(400, "Такого поста нету")

# schedule_bd = [

# ]

# class scheduleSchema(Schema):

#     id: int
#     subject: str
#     teacher: str
#     day: str
#     time: str

# @api.post("/lessons")
# def add_lesson(request, data: scheduleSchema):
#     lesson_id = data.id
#     for lesson in schedule_bd:
#         if lesson["id"] == lesson_id:
#             raise HttpError(400, "такой урок уже есть")
#     schedule_bd.append(data.dict())
#     return{"message": f"занятия по предмету {data.subject} добавленно"}

# @api.get("/lessons")
# def list_lesson(request):
#     return schedule_bd

# @api.put("/lessons/{id}")
# def chage_lisson(request, id: int, update_lesson: scheduleSchema):
#     for i, lesson in enumerate(schedule_bd):
#         if lesson["id"] == id:
#             lesson["day"] = update_lesson.day
#             lesson["time"] = update_lesson.time
#             return {"message": "день и время измененно"}
            
#     raise HttpError(404, "этого урока нету")

# @api.delete("/lessons/{id}")
# def delete_lesson(request, id: int):
#     for lesson in schedule_bd:
#         if lesson["id"] == id:
#             schedule_bd.remove(lesson)
#             return{"message": "урок удален"}
#     raise HttpError(404, "этого урока нету")


# schedule_bd = []

# class ScheduleSchema(Schema):
#     id: int
#     subject: str
#     teacher: str
#     day: str
#     time: str
#     students: list[str]

# @api.post("/lessons")
# def add_lesson(request, data: ScheduleSchema):
#     for lesson in schedule_bd:
#         if lesson["id"] == data.id:
#             raise HttpError(400, "Такой урок уже есть")
    
#     schedule_bd.append(data.dict())
#     return {"message": f"Занятие по предмету {data.subject} добавлено"}

# @api.get("/lessons")
# def list_lessons(request):
#     return schedule_bd

# @api.get("/lessons/{id}")
# def get_lesson(request, id: int):
#     for lesson in schedule_bd:
#         if lesson["id"] == id:
#             return lesson
#     raise HttpError(404, "Этого урока нету")

# @api.put("/lessons/{id}")
# def change_lesson(request, id: int, update_lesson: ScheduleSchema):
#     for i, lesson in enumerate(schedule_bd):
#         if lesson["id"] == id:
#             schedule_bd[i] = update_lesson.dict()
#             return {"message": "Урок обновлен"}
#     raise HttpError(404, "Этого урока нету")

# @api.delete("/lessons/{id}")
# def delete_lesson(request, id: int):
#     for lesson in schedule_bd:
#         if lesson["id"] == id:
#             schedule_bd.remove(lesson)
#             return {"message": "Урок удален"}
#     raise HttpError(404, "Этого урока нету")

# @api.post("/lessons/{id}/students")
# def add_student(request, id: int, name: str):
#     for lesson in schedule_bd:
#         if lesson["id"] == id:
#             if name in lesson["students"]:
#                 raise HttpError(400, "Студент уже есть в списке")
#             lesson["students"].append(name)
#             return {"message": f"Студент {name} успешно добавлен"}
            
#     raise HttpError(404, "Занятия с таким id нету")

# @api.delete("/lessons/{id}/students/{name}")
# def delete_student(request, id: int, name: str):
#     for lesson in schedule_bd:
#         if lesson["id"] == id:
#             if name in lesson["students"]:
#                 lesson["students"].remove(name)
#                 return {"message": f"Студент {name} успешно удален", "lesson": lesson}
#             else:
#                 raise HttpError(404, "Ученика нету")
                
#     raise HttpError(404, "Занятия с таким id нету")

# class StudentIn(Schema):
#     name: str
#     group: str
#     average_score: float


# class StudentOut(Schema):
#     id: int
#     name: str
#     group: str
#     average_score: float


# @api.post("/students")
# def create_student(request, data: StudentIn):
#     student = Student.objects.create(**data.model_dump())
#     return {"message": f"Студент {student.name} добавлен"}


# @api.get("/students", response=List[StudentOut])
# def get_students(request):
#     return Student.objects.all()


# @api.get("/students/{student_id}", response=StudentOut)
# def get_student(request, student_id: int):
#     student = Student.objects.filter(id=student_id).first()
#     if not student:
#         raise HttpError(404, "Студент не найден")
#     return student


# @api.put("/students/{student_id}")
# def update_student(request, student_id: int, updated: StudentIn):
#     student = Student.objects.filter(id=student_id).first()
#     if not student:
#         raise HttpError(404, "Студент не найден")
#     student.name = updated.name
#     student.group = updated.group
#     student.average_score = updated.average_score
#     student.save()
#     return {"message": "Данные студента обновлены"}


# @api.delete("/students/{student_id}")
# def delete_student(request, student_id: int):
#     student = Student.objects.filter(id=student_id).first()
#     if not student:
#         raise HttpError(404, "Студент не найден")
#     student.delete()
#     return {"message": "Студент удалён"}


# @api.get("/students/{student_id}", response=StudentOut)
# def get_student(request, student_id: int):
#     return get_object_or_404(Student, id=student_id)

# class TeacherIn(Schema):
#     name: str
#     subject: str
#     experience: int = Field(ge=0)

# class TeacherOut(Schema):
#     id: int
#     name: str
#     subject: str
#     experience: int

# @api.post("/teachers")
# def create_teacher(request, data: TeacherIn):
#     teacher = Teacher.objects.create(**data.model_dump())
#     return{"message": f"Учитель {teacher.name} добавлен"}

# @api.get("/teachers", response=List[TeacherOut])
# def get_teachers(request):
#     return Teacher.objects.all()

# @api.get("/teachers/{teachers_id}", response=TeacherOut)
# def get_teacher(request, teachers_id: int):
#     teacher = Teacher.objects.filter(id=teachers_id).first()
#     if not teacher:
#         raise HttpError(404, "Учитель не найден")
#     return teacher

# @api.put("/teachers/{teachers_id}")
# def update_teacher(request, teachers_id: int, update:TeacherIn):
#     teacher = Teacher.objects.filter(id=teachers_id).first()
#     if not teacher:
#         raise HttpError(404, "Учитель не найден")
#     teacher.name = update.name
#     teacher.subject = update.subject
#     teacher.experience = update.experience
#     teacher.save()
#     return {"message": "Данные учителя обновлены"}

# @api.delete("/teachers/{teacher_id}")
# def delete_teacher(request, teacher_id: int):
#     teacher = Teacher.objects.filter(id=teacher_id).first()
#     if not teacher:
#         raise HttpError(404, "Учитель не найден")
#     teacher.delete()
#     return{"message": "Учитель удален"}

# @api.get("/teachers/{teacher_id}", response=TeacherOut)
# def get_student(request, teacher_id: int):
#     return get_object_or_404(Teacher, id=teacher_id)


# from typing import List
# from ninja import NinjaAPI, Schema, Field
# from ninja.errors import HttpError
# from course.models import Course 

# api = NinjaAPI()

# class CourseIn(Schema):
#     title: str
#     duration: int = Field(..., gt=0)
#     teacher: str


# class CourseOut(Schema):
#     id: int
#     title: str
#     duration: int = Field(..., gt=0)
#     teacher: str


# @api.post("/course")
# def create_course(request, data: CourseIn):
#     course = Course.objects.create(**data.model_dump())
#     return{"message": f"Курс {course.title} добавлен"}

# @api.get("/course", response=List[CourseOut])
# def get_course(request):
#     return Course.objects.all()

# @api.put("/course/{course_id}")
# def updata_course(request, course_id: int, data: CourseIn):
#     course = Course.objects.filter(id=course_id).first()
#     if not course:
#         raise HttpError(322, "курса нет")
#     course.title = data.title
#     course.duration = data.duration
#     course.teacher = data.teacher
#     course.save()
#     return {"message": f"Курс {course.title} обновлен"}

# @api.delete("/course/{course_id}")
# def delete_course(request, course_id: int):
#     course = Course.objects.filter(id=course_id).first()
#     if not course:
#         raise HttpError(322, "курса нет")
#     course.delete()
#     return{"message": "Курс удален"}