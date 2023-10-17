from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import pandas

from file_handler.models import CSVFile
from file_handler.serializers import FileSerializer, ErrorAndStatusSerializer


class UploadFile(APIView):
    @extend_schema(summary="Загрузка файла", responses={status.HTTP_200_OK: FileSerializer})
    def put(self, request):
        file = CSVFile.objects.create(author=self.request.user, file=request.FILES['file'])
        return Response(data=FileSerializer(file).data, status=status.HTTP_201_CREATED)


class ListFiles(APIView):
    @extend_schema(summary="Список файлов", responses={status.HTTP_200_OK: FileSerializer})
    def get(self, request):
        """Получение списка всех файлов с информацией о колонках"""
        files = CSVFile.objects.all()
        data = []
        for file in files:
            serialized_file = FileSerializer(file).data
            serialized_file['fields'] = list(pandas.read_csv(file.file.path).columns)
            data.append(serialized_file)
        return Response(data=data)


class FileData(APIView):
    @extend_schema(summary="Получение данных из файла", responses={status.HTTP_200_OK: ErrorAndStatusSerializer,
                                                                   status.HTTP_404_NOT_FOUND: ErrorAndStatusSerializer})
    def get(self, request, *args, **kwargs):
        """ Получение данных из файла.
            Параметры запроса:
                id:     id файла
                filter: колонка для фильтрации (одна или несколько)
                sort:   колонка для сортировки (одна или несколько)"""
        pass


class FileDelete(APIView):
    @extend_schema(summary="Удаление файла", responses={status.HTTP_204_NO_CONTENT: ErrorAndStatusSerializer,
                                                        status.HTTP_404_NOT_FOUND: ErrorAndStatusSerializer})
    def delete(self, request, pk):
        """Удаление файла по переданному id"""
        try:
            obj = CSVFile.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CSVFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
