from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Contact
from .API.api import ContactViewSet,sending_email


class Test(TestCase):
    def setUp(self) -> None:
        self.test_obj = Contact.objects.create(first_name = "ali" , last_name = "az" , phone_number = "+989130741977" ,
                                               email = "aliazamian1@gmail.com")
        self.factory = APIRequestFactory()
        self.list_view = ContactViewSet.as_view({"get":"list" , "post":"create"})
        self.detail_view = ContactViewSet.as_view({"get":"retrieve" , "delete" : "destroy" ,
                                                   "put" : "update" , "patch" :"partial_update"})
        
        
    def testmodel(self):
        first_name_verbose = self.test_obj._meta.get_field('first_name').verbose_name
        self.assertEqual(first_name_verbose , "firstname")
        email_null = self.test_obj._meta.get_field("email").null
        self.assertTrue(email_null)
        
        
    def test_list_api(self):
        
        request = self.factory.get("/contact/")
        response = self.list_view(request)
        response.render()
        
        self.assertEqual(response.status_code , 200)
        
    def test_retrive_api(self):

        request = self.factory.get(f"/contact/{self.test_obj.slug}/")
        response = self.detail_view(request ,slug = self.test_obj.slug )
        response.render()
        
        self.assertEqual(response.status_code , 200)
        
    def test_post_api (self) :
        request = self.factory.post(self.list_view ,{"first_name":"sina" , "last_name" : "mamadi" , "phone_number" : "09133333333" 
                                             , "email":"a@a0com"},format = "json")
        response = self.list_view(request)
        response.render()
        self.assertEqual(response.status_code , 201) #object created ..!
        self.assertEqual(response.data.get("url"),'http://testserver/contact/sina/' )
        
        
    def test_delete_api(self):

        request = self.factory.delete(f"/contact/{self.test_obj.slug}/")
        response = self.detail_view(request ,slug = self.test_obj.slug  )
        response.render()
        
        self.assertEqual(response.status_code , 204) #object deleted ..!
        
    
    def test_put_api(self):
        
        request = self.factory.put(f"/contact/{self.test_obj.slug}/" , {"first_name":"mahsa" , "last_name" : "mahii",
                                                                        "phone_number" : self.test_obj.phone_number} , format = "json")
        response = self.detail_view(request , slug = self.test_obj.slug)
        response.render()

        self.assertEqual(response.status_code , 200)
        
        
    def test_patch_api(self):
        request = self.factory.patch(f"/contact/{self.test_obj.slug}/" , {"first_name":"mahsa" , "last_name" : "mahii"},
                                                                         format = "json")
        response = self.detail_view(request , slug = self.test_obj.slug)
        response.render()

        self.assertEqual(response.status_code , 200)
        
    
    def test_email(self):
        request = self.factory.post("/send-mail/" , {"email":"aliazamian1@gmailcom" , "message":"im sending"}, format = "json")
        response = sending_email(request)
        response.render()
        self.assertEqual(response.data , "email sended")
        self.assertEqual(response.status_code , 200)