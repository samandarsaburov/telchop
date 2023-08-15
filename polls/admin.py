from django.contrib import admin
from .models import TelChopModel
# Register your models here.
class TelAdmin(admin.ModelAdmin):
    list_display = ['model','tel_haqida','creat_date','update_date','del_date']
    search_fields =['model']

admin.site.register(TelChopModel, TelAdmin)
