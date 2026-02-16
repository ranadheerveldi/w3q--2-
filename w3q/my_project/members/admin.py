from django.contrib import admin

# Register your models here.
from .models import Member ,FormModel ,LoginUser
admin.site.register(Member)


#@admin.register(FormModel)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "phone", "joined_date")
    search_fields = ("firstname", "lastname", "phone")
    list_display_links = ("firstname", "lastname")
    fieldsets = (
        ("Personal Info", {"fields": ("firstname", "lastname", "phone")}),
        ("Membership Info", {"fields": ("joined_date",)}),
    )




# Register FormModel
admin.site.register(FormModel)
admin.site.register(LoginUser)