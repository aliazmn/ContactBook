from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    exclude = ("slug" ,)
    list_display = ("first_name" , "last_name" , "phone_number")
    list_filter = ("slug",)
    search_fields = ("first_name" , "last_name")