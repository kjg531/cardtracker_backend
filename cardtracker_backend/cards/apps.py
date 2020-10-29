from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CardsConfig(AppConfig):
    name = "cardtracker_backend.cards"
    verbose_name = _("Cards")

    def ready(self):
        try:
            import cardtracker_backend.cards.signals  # noqa F401
        except ImportError:
            pass
