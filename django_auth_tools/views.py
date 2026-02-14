from django.views.generic import TemplateView

from .mixins import NoLoginRequiredMixin


class IndexView(NoLoginRequiredMixin, TemplateView):
    template_name = "django_auth_tools/index.html"


class DashboardView(TemplateView):
    template_name = "django_auth_tools/dashboard.html"


class PublicView(NoLoginRequiredMixin, TemplateView):
    template_name = "django_auth_tools/public.html"
