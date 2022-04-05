from django. shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response
from contacts.models import Contact
from contacts.tasks import send_email


class ListContactSerializer(serializers.HyperlinkedModelSerializer):
    
    
    class Meta :
        model = Contact
        fields  = ("url","first_name" , "last_name" ,"phone_number","home_phone","email")
        extra_kwargs = {
        'url': {'view_name': 'contact:contacts-detail', 'lookup_field': 'slug'},
        'home_phone' : {"allow_blank" : True}
        }
        read_only_fields = ("slug" , )
        
        
class DetailContactSerializer(serializers.ModelSerializer):
    
    
    class Meta :
        model = Contact
        fields  = ("first_name" , "last_name" ,"phone_number" , "home_phone" , "email")
        extra_kwargs = {
        'home_phone' : {"allow_blank" : True}
        }
        read_only_fields = ("slug" , )

