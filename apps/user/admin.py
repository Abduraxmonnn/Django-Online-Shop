from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from apps.user.models import User

"""
A form for creating new users. Includes all the required fields, plus a repeated password.
"""
class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    """
    Check that the two password entries match
    """
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return confirm_password

    """
    Save the provided password in hashed format
    """

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user


"""
A form for updating users. Includes all the fields on
the user, but replaces the password field with admin's
password hash display field.
"""
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age', 'is_admin', 'is_superuser')

    """
    Regardless of what the user provides, return the initial value.
    This is done here, rather than on the field, because the field does not have access to the initial value
    """

    def clean_password(self):
        return self.initial['password']


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    The forms to add and change user instances
    """
    form = UserChangeForm
    add_form = UserCreationForm

    """
    these fields to be used in displaying the User model.
    These override the definitions on the base UserAdmin
    that reference specific fields on auth.User.
    """
    list_display = ('username', 'is_superuser', 'is_admin', 'age')
    list_filter = ('username', 'is_superuser', 'is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': (
            'is_admin', 'is_superuser', 'is_active',
            'first_name', 'last_name', 'email', 'age'
        )}),
    )

    """
    add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    overrides get_fieldsets to use this attribute when creating a user.
    """
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password', 'confirm_password'),
        }),
    )

    search_fields = ('username', 'first_name', 'last_name')
    ordering = ('username', )
