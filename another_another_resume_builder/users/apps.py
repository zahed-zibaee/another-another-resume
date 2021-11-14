from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "another_another_resume_builder.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import another_another_resume_builder.users.signals  # noqa F401
        except ImportError:
            pass
