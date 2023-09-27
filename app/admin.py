from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreateForm, CustomerChangeForm
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(UserAdmin):
  add_form = CustomerCreateForm
  form = CustomerChangeForm
  model = Customer
  list_display = ('register_number', 'first_name', 'last_name', 'is_staff')
  fieldsets = (
    (None, {'fields': ('email', 'password')}),
    ('Personal Information', {'fields': ('first_name', 'last_name')}),
    ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    ('Important Dates', {'fields': ('last_login', 'date_joined')})
  )
