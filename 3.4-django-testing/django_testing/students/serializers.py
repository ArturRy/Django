from rest_framework import serializers

from students.models import Course

from django_testing.settings import MAX_STUDENTS_PER_COURSE


class CourseSerializer(serializers.ModelSerializer):
    def validate_students(self, value):
        if len(value) > MAX_STUDENTS_PER_COURSE:
            raise serializers.ValidationError("Максимальное количество студентов 20")
        return value
    class Meta:
        model = Course
        fields = ("id", "name", "students")
