from django.db import models


class LVMModel(models.Model):
    volume_group = models.CharField(max_length=50)
    logical_volume = models.CharField(max_length=50)
    size = models.IntegerField()

    def __str__(self):
        return f'{self.volume_group} {self.logical_volume} {self.size}'
