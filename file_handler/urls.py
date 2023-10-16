from django.urls import path
from file_handler import views

app_name = 'file_handler'

urlpatterns = [
    path('list/', views.ListFiles.as_view(), name='list'),
    path('upload/', views.UploadFile.as_view(), name='upload'),
]