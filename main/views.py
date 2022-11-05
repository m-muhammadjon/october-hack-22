from rest_framework import generics
from rest_framework.filters import SearchFilter

from main import models, serializers


class AdvocateListView(generics.ListAPIView):
    queryset = models.Advocate.objects.all()
    serializer_class = serializers.AdvocateSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username',]


class AdvocateDetailView(generics.RetrieveAPIView):
    queryset = models.Advocate.objects.all()
    serializer_class = serializers.AdvocateSerializer
    lookup_field = 'username'

