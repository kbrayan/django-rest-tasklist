from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from tasklist.models import Task

from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    HTMLFormRenderer,
    BrowsableAPIRenderer,
    )

from rest_framework.response import Response

from .serializers import (
    TaskCreateSerializer,
    TaskUpdateSerializer,
    TaskDetailSerializer,
    TaskListSerializer,
    TaskDeleteSerializer,
    )

User = get_user_model()


class TaskListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tasklist/task-list-api.html'
    #
    def get(self, request):
        qs = Task.objects.all()
        serializer = TaskListSerializer(qs, many=True)
        return Response({'serializer': serializer, 'tasks': qs})


class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)



class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tasklist/task-create-api.html'

    def get(self):
        serializer = TaskCreateSerializer()
        return Response({'serializer': serializer})

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        messages.success(request, 'Task criada!')
        return redirect('tasklist-api:list')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskCreate2APIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    # lookup_field = 'uuid'
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tasklist/task-detail-api.html'

    def get(self):
    #     print('task_obj')
        task_obj = self.get_object()
        serializer = self.get_serializer(task_obj)
        return Response({'serializer': serializer, 'context': task_obj})

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        return get_object_or_404(Task, uuid=uuid)


class TaskUpdateAPIView(LoginRequiredMixin, RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUpdateSerializer
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tasklist/task-update-api.html'

    def retrieve(self):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'serializer': serializer, 'instance': instance})

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        return get_object_or_404(Task, uuid=uuid)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        messages.success(request, 'Sua task foi atualizada')
        return Response({'serializer': serializer, 'instance': instance, 'messages': messages})


class TaskDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDeleteSerializer
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tasklist/task-delete-api.html'

    def get_object(self):
        uuid = self.kwargs.get("uuid")
        try:
            return Task.objects.get(uuid=uuid)
        except:
            messages.warning(self.request, 'Task não encontrada!')
            return redirect('tasklist-api:list')

    def perform_destroy(self, instance):
        instance.delete()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            messages.error(request, 'Task apagada!')
            return redirect('tasklist-api:list')
        except:
            return redirect('tasklist-api:list')