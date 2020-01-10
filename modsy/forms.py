
from django import forms
from . models import user
from django.contrib.auth.models import User
from . models import User_Requirement
from . models import room
from . models import goal
from . models import design
from . models import furniture

class UserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('username','email','password')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')
        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email
            raise forms.ValidationError('This email address is already in use.')
class UserRequirementForm(forms.ModelForm):
    class Meta:
        model = User_Requirement
        fields=('room','goal','design','furniture')
