from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r"", include(("spekit_app.urls", "spekit_app"), namespace="api")),
]
