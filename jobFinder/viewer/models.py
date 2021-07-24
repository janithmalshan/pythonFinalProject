from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=75)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    # Assume one skill assigned to one category

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100)
    # company = models.ForeignKey
    publish_date = models.DateField(auto_now_add=True)
    expire_date = models.DateField()
    job_desc = models.TextField(null=True, blank=True)
    job_image = models.ImageField(upload_to='images/', null=True, blank=True)
    job_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    job_skills = models.ManyToManyField(Skill, null=True, blank=True)
    # Job has one category and multiple skills


    def __str__(self):
        return self.title
