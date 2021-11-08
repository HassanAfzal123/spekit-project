from django.urls import path, include
from rest_framework import routers
from .views import GetDocumentsViewSet, UploadViewSet, GetTopicsViewSet, GetFoldersViewSet, UpdateTopicViewSet, UpdateFolderViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")
router.register(r'getdocuments', GetDocumentsViewSet, basename="getdocuments")
router.register(r'get-topics', GetTopicsViewSet, basename="get-topics")
router.register(r'get-folders', GetFoldersViewSet, basename="get-folders")
router.register(r'update-folder', UpdateFolderViewSet, basename="update-folder")
router.register(r'update-topic', UpdateTopicViewSet, basename="update-topic")
urlpatterns = [
    path('', include(router.urls)),
]