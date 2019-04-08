import datetime
import requests, uuid
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
  uuid        = models.UUIDField(default=uuid.uuid4, editable=False)
  taskname    = models.CharField(max_length=60, blank=False, null=False)
  description = models.CharField(max_length=120, blank=False, null=False)
  content     = models.TextField(max_length=120, blank=False, null=False)
  due_date    = models.DateTimeField(auto_now=False, blank=True, null=True, auto_now_add=False)
  finished    = models.BooleanField(default=False, blank=False, null=False)
  finished_date = models.DateTimeField(auto_now=False, blank=True, null=True, auto_now_add=False)
  updated     = models.DateTimeField(auto_now=True, auto_now_add=False)
  created     = models.DateTimeField(auto_now_add=True)
  active      = models.BooleanField(default=True, blank=False, null=False)
  deletion_date = models.BooleanField(default=False, blank=False, null=False)

  def __str__(self):
    return self.taskname

  def get_api_url(self):
    return reverse("tasklist-api:detailUUID", kwargs={"uuid": self.uuid})

  def was_published_recently(self):
    return self.updated >= timezone.now() - datetime.timedelta(days=1)

  class Meta:
    ordering = ('-created',)
    verbose_name_plural = 'Tasks'
