from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    body = RichTextUploadingField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_posts', blank=True, null=True)
    recipients = models.ManyToManyField(User, related_name='received_posts', blank=True)
    deleted = models.BooleanField(default=False)



class Event(models.Model):
    name = models.CharField(_("Name"), max_length=200)
    description = models.TextField(_("Description"), blank=True)
    date = models.DateField(_("Date"), blank=True, null=True)
    time = models.TimeField(_("Time"), blank=True, null=True)
    deleted = models.BooleanField(_("Deleted"), default=False)

class Movie(models.Model):
    
    title = models.CharField(_("Title"), max_length=200)
    description = models.TextField(_("Description"), blank=True)
    release_date = models.DateField(_("Release Date"), blank=True, null=True)
    duration = models.IntegerField(_("Duration"), blank=True, null=True)
    deleted = models.BooleanField(_("Deleted"), default=False)

class Shopping(models.Model):
    
    product_name = models.CharField(_("Product Name"), max_length=200)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, blank=True, null=True)
    store = models.CharField(_("Store"), max_length=200, blank=True)
    deleted = models.BooleanField(_("Deleted"), default=False)

class Birthday(models.Model):
    person_name = models.CharField(_("Person Name"), max_length=200)
    birth_date = models.DateField(_("Birth Date"))
    gift_ideas = models.TextField(_("Gift Ideas"), blank=True)
    is_celebrated = models.BooleanField(_("Is Celebrated"), default=False)
    deleted = models.BooleanField(_("Deleted"), default=False)


class BlogPost(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    body = RichTextUploadingField()
    
    def __str__(self):
        return self.title
