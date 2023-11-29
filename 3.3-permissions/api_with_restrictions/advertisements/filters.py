from datetime import date

from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at_before = filters.DateFilter(field_name="created_at", lookup_expr="lte")
    created_at_after = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    status_open = filters.BooleanFilter(field_name="status", lookup_expr="OPEN")
    status_closed = filters.BooleanFilter(field_name="status", lookup_expr="CLOSED")

    class Meta:
        model = Advertisement
        fields = ["id"]
