from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import Detail
class Brand(ImportExportModelAdmin):
    pass
admin.site.register(Detail,Brand)
