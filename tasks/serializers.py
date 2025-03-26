# tasks/serializers.py
from rest_framework import serializers
from .models import Task, Comment
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority',
                  'category', 'state', 'owner', 'created_at', 'updated_at']

    def validate_due_date(self, value):
        if value < datetime.now():
            raise serializers.ValidationError(
                "The due date cannot be in the past.")
        return value



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'task', 'author', 'content', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'tasks']
