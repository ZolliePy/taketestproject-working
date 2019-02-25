from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User


class TestInfo(models.Model):
    TestName = models.CharField(max_length=255)
    MaxMarks = models.IntegerField()
    TimeDuration = models.IntegerField()
    PosMarks = models.IntegerField()
    NegMarks = models.IntegerField()
    InputTextFile = models.FileField(upload_to='Tests/',\
    validators=[FileExtensionValidator(allowed_extensions=['txt'])],blank=False)

    def __str__(self):
        return self.TestName
