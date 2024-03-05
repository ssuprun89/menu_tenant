from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from clients.serializers import ClientSerializer


class ClientViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    serializer_class = ClientSerializer

    def get_object(self):
        return self.request.tenant


