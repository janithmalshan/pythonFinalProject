from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    # company = models.ForeignKey
    publish_date = models.DateField()
    expire_date = models.DateField()
    active_days = models.IntegerField(max_length=62, default=31)
    # duration = models.PositiveIntegerField()
    # age_rating = models.CharField(max_length=5, default='G')
    # storyline = models.TextField(null=True, blank=True)
    # genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, null=True, blank=True)
    # rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title