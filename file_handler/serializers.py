from rest_framework import serializers

from file_handler.models import CSVFile


class FileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CSVFile
        fields = '__all__'


class UploadFIleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CSVFile
        fields = '__all__'
