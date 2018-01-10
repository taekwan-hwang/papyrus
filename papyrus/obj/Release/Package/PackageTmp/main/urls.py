from django.conf.urls import url
from main import views

urlpatterns = [
    url('tong6/', views.Tong6List.as_view())
]
