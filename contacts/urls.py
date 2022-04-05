from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .API.api import ContactViewSet , sending_email

app_name = "contacts"
router = DefaultRouter()

router.register(r'contact', ContactViewSet, basename='contacts')

urlpatterns = [
    path("send-mail/" , sending_email , name = "send")
    ]+router.urls
