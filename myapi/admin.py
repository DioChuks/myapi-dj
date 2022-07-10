from django.contrib import admin
from .models import Hero
from .models import Post
from .models import User
# Register your models here.

admin.site.register(Hero)
admin.site.register(Post)
admin.site.register(User)