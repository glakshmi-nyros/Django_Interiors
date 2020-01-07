
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import room
from .models import goal
from .models import design
from .models import user
from .models import furniture
from .models import UserRequirement

# Register your models here.

admin.site.register(room)
admin.site.register(goal)
admin.site.register(design)
admin.site.register(user)
admin.site.register(furniture)
admin.site.register(UserRequirement)
