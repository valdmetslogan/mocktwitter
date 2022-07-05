import py_compile
from django.contrib import admin

from .models import User, Posts, FollowJoin, Comments

admin.site.register(User)
admin.site.register(Posts)
admin.site.register(FollowJoin)
admin.site.register(Comments)

# Register your models here.
