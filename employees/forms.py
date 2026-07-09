from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width: 200px;',
                'placeholder': 'Enter location'
            }),
        }


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise forms.ValidationError("Phone number should contain only digits")

        if len(phone) != 10:
            raise forms.ValidationError("Phone number must be exactly 10 digits")

        return phone

    def clean_email(self):
        email = self.cleaned_data['email']

        qs = Employee.objects.filter(email=email)

        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise forms.ValidationError("This email already exists.")

        return email.lower()