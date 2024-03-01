from django import forms
from .models import User, DietaryRestriction

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'target_weight', 'current_weight', 'height', 'weekly_physical_activity', 'gender', 'dietary_restriction']
        widgets = {
            'dietary_restriction': forms.Select()
        }

