from django.urls import re_path

from dummy.consumers import DummyConsumer

websocket_urlpatterns = [
    re_path(r'ws/', DummyConsumer.as_asgi())
]