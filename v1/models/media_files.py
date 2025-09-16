from django.db import models


class MediaFileModel(models.Model):
    file = models.FileField(upload_to="uploads/%Y/%m/%d/")
    title = models.CharField(max_length=200, blank=True, null=True)
    alt = models.CharField(max_length=300, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    @property
    def url(self):
        return self.file.url

    def __str__(self):
        return self.title or self.file.name