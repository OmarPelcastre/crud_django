from django.contrib import admin
from Test1.models import testModel

class Test1(admin.ModelAdmin):
    pass
admin.site.register(testModel, Test1)