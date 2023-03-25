from rest_framework import generics
from ..Serialization import PositionSerialize
from ...models import Position


class PositionList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerialize.PositionSerializer


class PositionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerialize.PositionSerializer
