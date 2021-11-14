from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ResumeConfig(AppConfig):
    name = "another_another_resume_builder.resume"
    verbose_name = _("Resume")

    def ready(self):
        try:
            import another_another_resume_builder.resume.signals  # noqa F401
        except ImportError:
            pass
