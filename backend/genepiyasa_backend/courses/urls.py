from django.urls import path
from .views import SubtopicView, UserView

urlpatterns = [
    path('courses/', SubtopicView),
    path('users/', UserView)
]