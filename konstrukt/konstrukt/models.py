from django.db import models

# I win
DJANGO_FIELDS = (
    (str(obj).upper()[0:2], obj)
    for obj in dir(models) if obj.endswith('Field')
)


class FieldValue(models.Model):
    key = models.CharField(
        blank=False, null=False,
        max_length=10000, choices=DJANGO_FIELDS)
    value = models.CharField(blank=False, null=False, max_length=10000)
    model = models.ManyToManyField('Model', null=True, blank=True)

    def __unicode__(self):
        return self.key


class Model(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100)

    def __unicode__(self):
        return self.name


class View(models.Model):
    name = models.CharField(blank=False, null=False, max_length=500)

    def __unicode__(self):
        return self.name
