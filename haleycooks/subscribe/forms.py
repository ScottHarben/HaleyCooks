from django.forms import ModelForm, TextInput
from subscribe.models import Email

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        labels = {
            'first_name': (''),
            'email': (''),
        }
        widgets = {
            'first_name': TextInput(attrs={'placeholder':'First name'}),
            'email': TextInput(attrs={'placeholder':'Email'}),
        }
