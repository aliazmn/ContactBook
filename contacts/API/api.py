from rest_framework.decorators import api_view 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from .serializer import ListContactSerializer,DetailContactSerializer 
from contacts.models import Contact
from contacts.tasks import send_email
from .filter import ContactFilterSet


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_classes = {
        'list': ListContactSerializer,
        'create' :ListContactSerializer ,
        'retrieve': DetailContactSerializer,
        "update" :DetailContactSerializer ,
        "partial_update" :DetailContactSerializer ,
        "destroy" :DetailContactSerializer
    }
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ContactFilterSet
    search_fields = ['name','brand']
    
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action)
    
    
    
@api_view(["GET","POST"])
def sending_email(request):
    if request.method == "POST" : 
        send_email.delay( request.data.get("email") ,  request.data.get("message"))
        return Response("email sended")   

    return Response("hi its sending email part pls enter your email and message in a dict ")   

