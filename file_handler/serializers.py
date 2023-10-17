from rest_framework import serializers

from file_handler.models import CSVFile


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CSVFile
        fields = '__all__'


class ErrorAndStatusSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    details = serializers.CharField()
