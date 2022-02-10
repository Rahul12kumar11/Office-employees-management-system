from django import forms
from .models import Department, role

class DepartmentForm(forms.ModelForm):
    """Form definition for Dep."""

    class Meta:
        """Meta definition for Depform."""

        model = Department
        fields = '__all__'


class roleForm(forms.ModelForm):
    """Form definition for Dep."""

    class Meta:
        """Meta definition for Depform."""

        model = role
        fields = '__all__'
