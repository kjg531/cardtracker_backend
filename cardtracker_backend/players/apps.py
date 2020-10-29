from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PlayersConfig(AppConfig):
    name = "cardtracker_backend.players"
    verbose_name = _("Players")

    def ready(self):
        try:
            import cardtracker_backend.players.signals  # noqa F401
        except ImportError:
            pass
