from django.urls import path
from .views import file_list, upload_file, download_file, generate_api_key, FileList, FileDetail

urlpatterns = [
    path('list/', file_list, name='file_list'),
    path('upload/', upload_file, name='upload_file'),
    path('download/<int:file_id>/', download_file, name='download_file'),
    path('generate-api-key/', generate_api_key, name='generate_api_key'),
    path('api/files/', FileList.as_view(), name='file-list'),
    path('api/files/<int:pk>/', FileDetail.as_view(), name='file-detail'),

]
