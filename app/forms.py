from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Customer


class CustomerCreateForm(UserCreationForm):

  class Meta:
    model = Customer
    fields = ('first_name', 'last_name')
    labels = {'username': 'CPF/CNPJ'}

  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    user.register_number = self.cleaned_data['username']
    
    if commit:
      user.save()
    
    return user
  

class CustomerChangeForm(UserChangeForm):

  class Meta:
    model = Customer
    fields = ('first_name', 'last_name')
