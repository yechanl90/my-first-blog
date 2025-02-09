from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='post_list'),  # 빈 문자열을 처리하는 방법
]
