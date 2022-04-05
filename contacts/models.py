from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext as _
from .validators import PhoneValidator ,HomePhone
from django.utils.text import slugify


class Contact (models.Model):
    first_name = models.CharField(max_length = 255 , verbose_name = _("firstname"))
    last_name = models.CharField(max_length = 255 , verbose_name = _("lastname"))
    phone_number = PhoneValidator()
    home_phone = HomePhone(null = True , blank = True)
    slug = models.SlugField(null = True , blank = True )
    email = models.EmailField(null = True)    
    created_date = models.DateTimeField(auto_now_add = True)
    
    
    class Meta :
        ordering = ['-created_date']
        verbose_name = "contact"
        verbose_name_plural = "contacts"

    
    
    def save(self,*args, **kwargs) -> None:
        if not self.slug :
            self.slug = slugify(value = self.first_name ,allow_unicode = True)        
        return super().save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}"
    
    