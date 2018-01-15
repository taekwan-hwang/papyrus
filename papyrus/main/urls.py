from django.conf.urls import url
from main import views

urlpatterns = [
    url('testgetbycycle', views.TestGetByCycle.as_view()),
    url('testgetbyperson', views.TestGetByPerson.as_view())
]
