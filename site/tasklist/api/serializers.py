from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    HiddenField,
    CharField,
    DateTimeField,
)
from tasklist.models import Task

User = get_user_model()

task_detail_url = HyperlinkedIdentityField(
    # read_only=True,
    view_name='tasklist-api:detailUUID',
    lookup_field='uuid',
    # lookup_url_kwarg='uuid'
)

task_delete_url = HyperlinkedIdentityField(
    # read_only=True,
    view_name='tasklist-api:deleteUUID',
    lookup_field='uuid'
    # lookup_url_kwarg='owner'
)

class DateTimeFieldWihTZ(serializers.DateTimeField):
    def to_representation(self, value):
        value = timezone.localtime(value)
        return super(DateTimeFieldWihTZ, self).to_representation(value)


class TaskListSerializer(ModelSerializer):
    url = task_detail_url
    delete_url = task_delete_url
    due_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Task
        fields = [
            'uuid',
            'taskname',
            'content',
            'description',
            'due_date',
            'finished',
            'updated',
            'created',
            'active',
            'url',
            'delete_url',
        ]


class TaskCreateSerializer(ModelSerializer):
    due_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Task
        fields = [
            'taskname',
            'content',
            'description',
            'due_date'
        ]

    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task


class TaskDetailSerializer(ModelSerializer):
    updated = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    due_date = DateTimeFieldWihTZ(format='%Y-%m-%d %H:%M')
    delete_url = task_delete_url

    class Meta:
        model = Task
        fields = [
            'uuid',
            'taskname',
            'content',
            'description',
            'due_date',
            'finished',
            'updated',
            'created',
            'delete_url',
        ]
        # read_only_fields = ['uuid']


class TaskUpdateSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'taskname',
            'content',
            'description',
            'finished',
        ]


class TaskDeleteSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'uuid',
        ]
