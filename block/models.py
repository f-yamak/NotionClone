from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    priority = models.IntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    links = models.ManyToManyField('self', symmetrical=False, blank=True)
    file_attachments = models.FileField(upload_to='blog_attachments/', blank=True)
    assignees = models.ManyToManyField(User, related_name='assigned_blogs', blank=True)
    notes = models.TextField(blank=True)
    images = models.ImageField(upload_to='blog_images/', blank=True)
    subpages = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='parent_blog')
    tasks = models.ManyToManyField('Task', related_name='blog_tasks', blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_blogs', blank=True, null=True)
    recipients = models.ManyToManyField(User, related_name='received_blogs', blank=True)

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
 