import enum


class Course(enum.Enum):
    EnumAngular = "Angular + NodeJS"
    EnumVue = "VueJS + NodeJS"
    EnumReact = "ReactJS + Golang"


def register(course: Course):
    print("Register : " + course.value)


course: Course = Course.EnumAngular
course = Course.EnumReact
print(course.value)
register(course)

if hasattr(Course, "EnumVue"):
    print("yes")
else:
    print("no")
