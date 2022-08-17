from django.contrib import admin
from .models import Administrator, Member, Area, Post 
from .models import Person

# Register your models here.

admin.site.register(Person)
admin.site.register(Member)
admin.site.register(Administrator)
admin.site.register(Area)
admin.site.register(Post)