from django.urls import path
from .import views


app_name = 'myapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sample/', views.Index2View.as_view(), name='index2'),
    path('test/', views.TestView.as_view(), name='test'),
]