from django.conf import settings
from django.apps import AppConfig


class GizmoConfig(AppConfig):
    name = "apps.gizmo"
    verbose_name = "Gizmo"

    def ready(self):
        # pylint: disable=unused-import
        # pylint: disable=import-outside-toplevel
        from . import signals

        if settings.DEBUG:
            print("Loaded aperture signals")
