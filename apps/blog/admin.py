from django.contrib import admin
from .models import Administrator, Member, Area, Post

# Register your models here.

# admin.site.register(Persons)
admin.site.register(Member)
admin.site.register(Administrator)
admin.site.register(Area)
admin.site.register(Post)