from django.contrib import admin
from .models import Profile,Relationship,Message

# Register your models here.

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Message)
