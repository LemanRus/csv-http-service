from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

import pandas

from file_handler.models import CSVFile
from file_handler.serializers import FileListSerializer, UploadFIleSerializer


class UploadFile(APIView):
    def post(self, request):
        file = CSVFile.objects.create(author=self.request.user, file=request.FILES['file'])
        return Response(data=UploadFIleSerializer(file).data)


class ListFiles(APIView):
    def get(self, request):
        files = CSVFile.objects.all()
        data = [FileListSerializer(file) for file in files]
        return Response(data=data)

