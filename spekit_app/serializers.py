from rest_framework.serializers import Serializer, FileField, CharField

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    folder_name = CharField()
    topic_name = CharField()
    class Meta:
        fields = ['file_uploaded','folder_name','topic_name']

class GetDocumentsSerializer(Serializer):
    folder_name = CharField()
    topic_name = CharField()
    class Meta:
        fields = ['folder_name','topic_name']

class UpdateTopicSerializer(Serializer):
    topic_name = CharField()
    new_topic_name = CharField()
    class Meta:
        fields = ['topic_name', 'new_topic_name']

class UpdateFolderSerializer(Serializer):
    folder_name = CharField()
    new_folder_name = CharField()
    folder_description = CharField()
    class Meta:
        fields = ['folder_name','new_folder_name','folder_description']