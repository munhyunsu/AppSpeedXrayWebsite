from django.db import models


# Create your models here.
class Xray(models.Model):
    # app_title = models.CharField('app title', max_length=255)
    package_name = models.CharField('package name', max_length=255)
    experiment_date = models.DateField('experimented date')
    scene_start = models.FloatField('scene start seconds')
    scene_end = models.FloatField('scene end seconds')
    raw_si = models.FloatField('raw value for speed index')
    raw_fp = models.FloatField('raw value for first paint')
    raw_cs = models.FloatField('raw value for cpu stable time')
    raw_ll = models.FloatField('raw value for layout load time')
    raw_rt = models.FloatField('raw value for rendering time after data download')
    ps = models.FloatField('performance score')
    per_si = models.FloatField('percentile for speed index')
    per_fp = models.FloatField('percentile for first paint')
    per_cs = models.FloatField('percentile for cpu stable time')
    per_ll = models.FloatField('percentile for layout load time')
    per_rt = models.FloatField('percentile for rendering time after data download')

    def __str__(self):
        return '{0} - {1}, {2}'.format(self.package_name,
                                       self.experiment_date,
                                       self.scene_start)
