from rest_framework.test import APIClient
import pytest
from model_bakery import baker

from students.models import Course, Student




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
    response = client.get('/api/v1/courses/?name=')
    if response.status_code == 200:
        assert len(response.json()) > 0
        index = response.json()[0]['id'] - 1
        assert response.json()[0]['name'] == Course.objects.all()[index].name


@pytest.mark.django_db
def test_create_course(client, student):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'test_name', 'student': student.id})
    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses_update = course_factory()
    response = client.patch('/api/v1/courses/1/', data={'name': 'test_name'})
    assert response.status_code == 200
    assert Course.objects.all()[0].name == 'test_name'

@pytest.mark.django_db
def test_delete_courses(client, course_factory):
    courses_delete = course_factory(_quantity=10)
    count = Course.objects.count()
    response = client.delete('/api/v1/courses/3/')
    assert response.status_code == 204
    assert Course.objects.count() == count - 1


