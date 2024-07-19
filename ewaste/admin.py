from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Registration)
admin.site.register(Category)
admin.site.register( Waste_mat)
admin.site.register(Total_cat)

# from import_export.admin import ExportActionMixin

# # Register your models here.
# class BookAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ('title', 'waste_name', 'waste_cost', 'category_name')
