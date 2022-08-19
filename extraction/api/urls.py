from django.urls import path

from extraction.api.views import UploadedDocumentList

urlpatterns = [
    path('api/v1/uploaded-documents/', UploadedDocumentList.as_view()),
]
