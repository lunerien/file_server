from django.shortcuts import render

# files/views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import File
from django.http import FileResponse
import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import FileSerializer, CustomUserSerializer


def file_list(request):
    files = File.objects.all()
    return render(request, 'files/file_list.html', {'files': files})


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'files/upload_file.html', {'form': form})


def download_file(request, file_id):
    file = File.objects.get(pk=file_id)
    file_path = file.file.path
    response = FileResponse(open(file_path, 'rb'))
    return response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_api_key(request):
    user = request.user
    user.api_key = CustomUser.objects.make_random_password()
    user.save()
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)


class FileList(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]
