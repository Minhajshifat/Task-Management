from django.contrib import admin
from category.models import TaskCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}
    list_display = [
        "category_name",
        "slug",
    ]  # admin a name and slug field onujai dekhabe


admin.site.register(TaskCategory, CategoryAdmin)
