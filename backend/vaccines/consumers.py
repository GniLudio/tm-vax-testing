from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer.generics import (
    ObserverModelInstanceMixin,
)

from vaccines.models import Vaccine
from vaccines.serializers import VaccineSerializer


class VaccineConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    lookup_field = "pk"
