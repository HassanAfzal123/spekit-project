from os import stat
from rest_framework import serializers
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from .serializers import UploadSerializer, GetDocumentsSerializer, UpdateFolderSerializer, UpdateTopicSerializer
from .models import Documents, Folders, Topics
from django.http import FileResponse
import zipfile
import io

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        fs = FileSystemStorage(location="media/")
        filename = fs.save(file_uploaded.name, file_uploaded)
        content_type = file_uploaded.content_type

        try:
            folder_name = request.data["folder_name"]
            topic_name = request.data['topic_name']
        except Exception as e:
            return Response(data = {"Status":"failure", "msg": "Invalid Data !"}, status = 422)

        folder_id = Folders.objects.filter(folder_name=folder_name).only('folder_id')
        topic_id = Topics.objects.filter(topic_name=topic_name).only('topic_id')

        #If folder name does not exists in db
        if not folder_id:
            folder = Folders(folder_name = folder_name, folder_description = "")
            folder.save(force_insert=True)
            folder_id = folder.folder_id

        #If topic name does not exists in db
        if not topic_id:
            topic = Topics(topic_name = topic_name)
            topic.save(force_insert=True)
            topic_id = topic.topic_id

        doc = Documents(doc_name = filename, doc_path = f"media/{filename}", folder_id_id= folder_id, topic_id_id=topic_id)
        doc.save(force_insert=True)
        
        response = "POST API and you have uploaded a {} file named {}".format(content_type,filename)
        return Response(response)
    
class GetDocumentsViewSet(ViewSet):
    serializer_class = GetDocumentsSerializer
    
    def list(self, request):
        try:
            folder_name = request.data["folder_name"]
            topic_name = request.data['topic_name']
        except Exception as e:
            return Response(data = {"Status":"failure", "msg": "Invalid Data !"}, status = 422)
        
        try:
            topic_id = Topics.objects.filter(topic_name=topic_name).only('topic_id').values()[0]["topic_id"]

            folder_id = Folders.objects.filter(folder_name=folder_name).only('folder_id').values()[0]["folder_id"]

        except Exception as e:
            folder_id = ''
            topic_id = ''

        if folder_id == '' or topic_id == '':
            return Response({"msg": "There are no documents in the given folder name and topic"})

        documents = Documents.objects.filter(topic_id=topic_id, folder_id=folder_id).select_related('folder_id','topic_id')
        
        if len(documents)>0:
            # create a ZipFile object
            stream = io.StringIO()
            zipObj = zipfile.ZipFile("files.zip", 'w')

            for doc in documents.values():
                print(doc["doc_path"])
                ##At this like it gives me error
                zipObj.write(doc["doc_path"])
            
            # close the Zip File
            zipObj.close()

            filepointer = open("files.zip", 'rb')
            response = FileResponse(filepointer,"application/zip")
            response['Content-Disposition'] = f'attachment; filename=files.zip'
            return response
        else:
            return Response({"status":"success","msg": "There are no documents in the given folder name and topic"})

class GetTopicsViewSet(ViewSet):

    def list(self, request):
        try:
            topic_name = request.data['topic_name']
        except Exception as e:
            topic_name = ''

        if topic_name == '':
            topics = Topics.objects.all().values()
        else:
            topics = Topics.objects.filter(topic_name=topic_name).values()

        return Response({"status":"success", "msg": topics})

class GetFoldersViewSet(ViewSet):

    def list(self, request):
        try:
            folder_name = request.data['folder_name']
        except Exception as e:
            folder_name = ''

        if folder_name == '':
            folders = Folders.objects.all().values()
        else:
            folders = Folders.objects.filter(folder_name=folder_name).values()

        return Response({"status":"success", "msg": folders})

class UpdateTopicViewSet(ViewSet):

    serializer_class = UpdateTopicSerializer

    def create(self, request):
        
        try:
            topic_name= request.data["topic_name"]
            new_topic_name = request.data['new_topic_name']

        except Exception as e:
            return Response(data = {"Status":"failure", "msg": "Invalid Data !"}, status = 422)

        try:
            Topics.objects.filter(topic_name=topic_name).update(topic_name=new_topic_name)
        except Exception as e:
            return Response({"Status":"failure", "msg": "No such topic found !"})

        return Response({"Status":"success", "msg": f"Topic {topic_name} updated to {new_topic_name}"})

class UpdateFolderViewSet(ViewSet):

    serializer_class = UpdateFolderSerializer

    def create(self, request):

        try:
            folder_name= request.data["folder_name"]
            new_folder_name = request.data['new_folder_name']
            folder_description = request.data['folder_description']

        except Exception as e:
            return Response(data = {"Status":"failure", "msg": "Invalid Data !"}, status = 422)

        try:
            Folders.objects.filter(folder_name=folder_name).update(folder_name=new_folder_name, folder_description=folder_description)
        except Exception as e:
            return Response({"Status":"failure", "msg": "No such folder found !"})

        return Response({"Status":"success", "msg": f"Folder information updated successfully !"})

