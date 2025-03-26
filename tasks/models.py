# # ytasks/models.py
# from django.contrib.auth.models import User
# from django.db import models


# class Task(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     priority = models.CharField(max_length=20, choices=[(
#         'low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
#     category = models.CharField(max_length=50)
#     state = models.CharField(max_length=20, choices=[(
#         'todo', 'To Do'), ('in_progress', 'In Progress'), ('done', 'Done')])
#     owner = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='tasks')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Comment(models.Model):
#     task = models.ForeignKey(
#         Task, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


#tasks/models.py

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=20, choices=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ])
    state = models.CharField(max_length=20, choices=[
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], default='open')
    is_overdue = models.BooleanField(default=False)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(
        Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"
