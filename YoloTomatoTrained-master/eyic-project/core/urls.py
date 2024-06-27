from django.urls import path
from django.urls import path
from .views import *


app_name = "core"

urlpatterns = [
    path("farm-video-upload/", farm_video_upload, name="farm_video_upload"),
    path("your-results/", your_results, name="your_results"),
    path("results/<int:request_id>/", results, name="results"),
    path("", index, name="index"),
]
