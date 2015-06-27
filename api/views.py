import django_filters
from rest_framework import viewsets, filters
from rest_framework_extensions.mixins import DetailSerializerMixin
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import (
    BirdSerializer, PermutationSerializer, PermutationTypeSerializer,
    PermutationTypeDetailSerializer)

from birds.models import Bird, BirdPermutation, PermutationType


class BirdFilter(
        CacheResponseMixin,
        django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='icontains')
    object_type = django_filters.MethodFilter(action='get_object_type')

    class Meta:
        model = Bird
        fields = ('name', 'parent', 'vispedia_id', 'object_type')

    def get_object_type(self, qs, value):
        if value in ['leafs', 'branches']:
            return getattr(qs, value)()
        return qs


class BirdViewSet(
        CacheResponseMixin,
        viewsets.ModelViewSet):
    queryset = Bird.objects.order_by('id')
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = BirdFilter
    serializer_class = BirdSerializer

    def filter_queryset(self, queryset):
        qs = super(BirdViewSet, self).filter_queryset(queryset)
        if 'parent' in self.request.QUERY_PARAMS:
            filter_value = self.request.QUERY_PARAMS['parent']
            if not filter_value:
                qs = qs.filter(parent=None)
        return qs


class PermutationViewSet(
        CacheResponseMixin,
        viewsets.ModelViewSet):
    queryset = BirdPermutation.objects.all()
    serializer_class = PermutationSerializer


class PermutationTypeViewSet(
        CacheResponseMixin,
        DetailSerializerMixin,
        viewsets.ModelViewSet):
    queryset = PermutationType.objects.all()
    serializer_class = PermutationTypeSerializer
    serializer_detail_class = PermutationTypeDetailSerializer
