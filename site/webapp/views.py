from django.contrib.auth import get_user_model
from django.views.generic import TemplateView

User = get_user_model()

class HomePageView(TemplateView):
    template_name = "webapp/home.html"