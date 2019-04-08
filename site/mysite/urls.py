from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('webapp.urls', namespace="webapp")),
    url(r'^contas/', include('allauth.urls')),
    url(r'^tarefas/', include('tasklist.api.urls', namespace="tasklist-api")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
