from rest_framework.test import APIClient
from rest_framework.exceptions import ValidationError
import pytest
from model_bakery import baker

from students.models import Course, Student

from students.serializers import CourseSerializer


# def test_example():
#     assert False, "Just test example"

@pytest.fixture
def student():
    return Student.objects.create()
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory
@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_course(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/1/')
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == course[0].id
# #
#
@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses_get = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses_get)




@pytest.mark.django_db
def test_courses_id_filter(client, course_factory):
    courses_filter = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/?id=6')
    if response.status_code == 200:
        index = response.json()[0]['id'] - 1
        assert response.json()[0]['id'] == Course.objects.all()[index].id

@pytest.mark.django_db
def test_courses_name_filter(client, course_factory):
    courses_name_filter = course_factory(_quantity=10)
    response = client.get(f"/api/v1/courses/?name={courses_name_filter[3].name}")
    data = response.json()

    assert response.status_code == 200
    assert data[0]["name"] == courses_name_filter[3].name



@pytest.mark.django_db
def test_create_course(client, student):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test_name', 'student': student.id})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses_update = course_factory(_quantity=1)
    response = client.patch(
        f"/api/v1/courses/{courses_update[0].id}/", data={"name": "test_name"}
    )
    assert response.status_code == 200
    assert Course.objects.all()[0].name == "test_name"


@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    courses_delete = course_factory(_quantity=1)
    count = Course.objects.count()
    response = client.delete(f"/api/v1/courses/{courses_delete[0].id}/")
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


test_values = [
    (21, pytest.raises(ValidationError))
]


@pytest.mark.django_db
@pytest.mark.parametrize("students_count, expected_result", test_values)
def test_validation(student_factory, students_count, expected_result):
    students_id = [student.id for student in student_factory(_quantity=students_count)]

    with expected_result:
        assert CourseSerializer().validate_students(value=students_id)