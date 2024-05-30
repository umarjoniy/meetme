from django.db import models

from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Technologies(models.Model):
    name = models.CharField(max_length=50)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    name_for_css = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CV(models.Model):
    description = models.CharField(max_length=100)
    filename = models.CharField(max_length=60)
    cv = models.FileField(upload_to='cv')

    def __str__(self):
        return self.description


class Statistic(models.Model):
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=8)
    css_style = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=25)
    job_title = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    period = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=25)
    position_degree = models.CharField(max_length=25)
    location = models.CharField(max_length=25)
    period = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class ProjectImages(models.Model):
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects')

    def __str__(self):
        return self.description


class Projects(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(null=True, blank=True)
    small_description = models.CharField(max_length=50)
    description = models.TextField()
    images = models.ManyToManyField(ProjectImages)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title


class Me(models.Model):
    name = models.CharField(max_length=30, verbose_name="First Name")
    lastname = models.CharField(max_length=30, verbose_name="Last Name")
    birthdate = models.DateField(verbose_name="Birthdate")
    address = models.CharField(max_length=60)

    photo = models.ImageField(upload_to='personal')
    cv = models.ForeignKey(CV, on_delete=models.PROTECT)

    phone_number = models.CharField(max_length=30, verbose_name="Phone Number")
    email = models.CharField(max_length=50, verbose_name="Email")
    job_title = models.CharField(max_length=100, verbose_name="Job Title")

    short_description = models.CharField(max_length=200, verbose_name="Short Description")
    description = models.TextField(verbose_name="Description")

    technologies = models.ManyToManyField(Technologies, verbose_name='Technologies')
    statistics = models.ManyToManyField(Statistic, verbose_name="Statistics")
    social_media = models.ManyToManyField(SocialMedia, verbose_name='Social Media')

    experience = models.ManyToManyField(Experience, verbose_name="Experience", blank=True)
    education = models.ManyToManyField(Education, verbose_name="Education", blank=True)
    projects = models.ManyToManyField(Projects, verbose_name="Projects", blank=True)

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Projects)
def project_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
