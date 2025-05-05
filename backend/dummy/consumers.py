from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from dummy.models import Dummy
from dummy.serializers import DummySerializer


class DummyConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Dummy.objects.all()
    serializer_class = DummySerializer
    lookup_field = "pk"