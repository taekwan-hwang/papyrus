from django.conf.urls import url
from main import views

urlpatterns = [
    url('testgetbycycle', views.TestGetByCycle.as_view()),
    url('testgetbyperson', views.TestGetByPerson.as_view()),
    url('testmeanpainvariance', views.TestVarianceMean.as_view()),
    url('tong2/(?P<pi>[0-9]+)', views.Tong2View.as_view()),
    url('tong5/(?P<pi>[0-9]+)', views.Tong5View.as_view()),
    url('tong8/(?P<pi>[0-9]+)', views.Tong8View.as_view())
]
