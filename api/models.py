from django.db import models

MEDIA_TYPE = (
    ('MP4', 'Mp4',),
    ('MP3', 'Mp3',),
    ('MKV', 'Mkv',),
    ('AVI', 'Avi',),
    ('TS', 'Ts',),

)

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=1000)
    media_type = models.CharField(choices=MEDIA_TYPE, max_length=5)

    def __str__(self):
        return self.name 