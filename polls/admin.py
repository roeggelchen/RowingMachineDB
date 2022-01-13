from django.contrib import admin

# Register your models here.

from .models import RowingSession
from .models import RowingStroke

admin.site.register(RowingSession)
admin.site.register(RowingStroke)