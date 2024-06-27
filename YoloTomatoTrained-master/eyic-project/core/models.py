from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
video_render_status = (
    ("completed", "completed"),
    ("processing", "processing"),
)



class Crop(models.Model):
    name=models.CharField(max_length=30)
    
    ph_farm_less=models.PositiveBigIntegerField()
    ph_farm_more=models.PositiveBigIntegerField()

    moisture_farm_less=models.PositiveBigIntegerField()
    moisture_farm_more=models.PositiveBigIntegerField()

    temperature_farm_less=models.PositiveBigIntegerField()
    temperature_farm_more=models.PositiveBigIntegerField()

    total_amt_salt_farm_less=models.PositiveBigIntegerField()
    total_amt_salt_farm_more=models.PositiveBigIntegerField()


    def __str__(self):
        return self.name

class FarmVideo(models.Model):
    user = models.ForeignKey(User, related_name="farm_videos", on_delete=models.CASCADE)
    video = models.FileField(
        upload_to="videos_uploaded",
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )
    ph_farm=models.FloatField()
    moisture_farm=models.FloatField()
    temperature=models.PositiveBigIntegerField()
    total_amt_salt=models.PositiveBigIntegerField()

    
    status = models.CharField(
        verbose_name="Status",
        default="processing",
        choices=video_render_status,
        max_length=10,
    )    
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "FarmVideo"
        verbose_name_plural = "FarmVideos"



class VideoFarmImages(models.Model):
    farm_video = models.ForeignKey(
        FarmVideo, related_name="video_farm_images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="video_farm_images")


    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "VideoFarmImages"
        verbose_name_plural = "VideoFarmImagess"




class Disease(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to="disease_images",null=True)

    def __str__(self):
        return self.name


class DetactFarmImages(models.Model):
    farm_images = models.ForeignKey(
        VideoFarmImages, related_name="detact_farm_images", on_delete=models.CASCADE
    )
    disease_detected = models.ManyToManyField(
        Disease, related_name="frame_disease", blank=True
    )

    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        verbose_name = "DetactFarmImages"
        verbose_name_plural = "DetactFarmImagess"
