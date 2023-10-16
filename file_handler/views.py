from django.shortcuts import render
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pandas

from file_handler.models import CSVFile
from file_handler.serializers import FileListSerializer, UploadFIleSerializer


class UploadFile(APIView):
    def put(self, request):
        file = CSVFile.objects.create(author=self.request.user, file=request.FILES['file'])
        return Response(data=UploadFIleSerializer(file).data, status=status.HTTP_201_CREATED)


class ListFiles(APIView):
    def get(self, request):
        files = CSVFile.objects.all()
        data = []
        for file in files:
            serialized_file = UploadFIleSerializer(file).data
            serialized_file['fields'] = list(pandas.read_csv(file.file.path).columns)
            data.append(serialized_file)
        return Response(data=data)


class FileDelete(DestroyAPIView):
    queryset = CSVFile.objects.all()
    serializer_class = FileListSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Deleted successfully"
        },
            status=status.HTTP_200_OK)
