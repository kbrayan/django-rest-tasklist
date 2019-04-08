from django.conf.urls import url

from .views import (
    TaskListAPIView,
    TaskAPIView,
    TaskCreateAPIView,
    TaskCreate2APIView,
    TaskDetailAPIView,
    TaskDeleteAPIView,
    TaskUpdateAPIView,
)

urlpatterns = [
    url(r'^list/$', TaskListAPIView.as_view(), name='list'),
    url(r'^list2/$', TaskAPIView.as_view(), name='list2'),
    url(r'^create/$', TaskCreateAPIView.as_view(), name='create'),
    url(r'^create2/$', TaskCreate2APIView.as_view(), name='create2'),
    url(r'^(?P<uuid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/$',
        TaskDetailAPIView.as_view(), name='detailUUID'),
    url(r'^(?P<uuid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/edit/$',
        TaskUpdateAPIView.as_view(), name='updateUUID'),
    url(r'^(?P<uuid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})/delete/$',
        TaskDeleteAPIView.as_view(), name='deleteUUID'),

]