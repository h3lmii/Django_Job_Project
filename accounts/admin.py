from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import SignUpForm,UserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
	add_form = SignUpForm
	form = UserChangeForm
	model = CustomUser
	list_display = [
	"email",
	"username",
	"resume",
	"first_name",
	"is_staff",
	]
	#fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("account_type",)}),)
	fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'username')}),)
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','username','email', 'password1', 'password2','resume'),}),)

	#add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("account_type",)}),)


# Register your models here.


admin.site.register(CustomUser, CustomUserAdmin)
