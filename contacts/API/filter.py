from django_filters.rest_framework import FilterSet
from contacts.models import Contact


class ContactFilterSet(FilterSet):
    class Meta:
        model = Contact
        fields = {
            'first_name': ['icontains'],
            'last_name':['icontains'],
            'phone_number' :['icontains']

        }