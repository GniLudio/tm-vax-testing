from django.urls import re_path

from vaccines import consumers


websocket_urlpatterns = [
    re_path(r"ws/vaccines/vaccine/$", consumers.VaccineConsumer.as_asgi()),
]
