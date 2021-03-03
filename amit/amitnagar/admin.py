from django.contrib import admin
from .models import *
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=["name","price","category"]
    

class AdminCategory(admin.ModelAdmin):
    list_display=["name"]

admin.site.register(Todolist)
admin.site.register(Employee)
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)