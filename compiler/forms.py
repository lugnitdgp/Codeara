from django import forms




class UserForm(forms.ModelForm):
    class Meta:
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image',
        ]        