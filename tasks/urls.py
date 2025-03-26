from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, LoginView, ProfileView, TaskCreateView, CommentCreateView, ActivityLogView


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('tasks/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/<int:task_id>/comments/', CommentCreateView.as_view(), name='task-comments'),
    path('activity/', ActivityLogView.as_view(), name='activity-log'),

]
