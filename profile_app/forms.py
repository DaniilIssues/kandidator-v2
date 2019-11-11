from profile_app.models import  Account
from django import forms


class EditForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['user'].required = False
        self.fields['status'].required = False
        self.fields['created'].required = False
        self.fields['progress'].required = False
        self.fields['text_to_sms'].widget = forms.Textarea()
        self.fields['text_to_email'].widget = forms.Textarea()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
