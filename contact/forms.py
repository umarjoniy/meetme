from django.forms import ModelForm
from .models import Contact, Subscribers


class FormContact(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        def __int__(self, *args, **kwargs):
            super(FormContact, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widgets.attrs['class'] = 'form-control'


class FormSubscribers(ModelForm):
    class Meta:
        model = Subscribers
        fields = "__all__"

        def __int__(self, *args, **kwargs):
            super(FormSubscribers, self).__init__(*args, **kwargs)
            for field_name, fields in self.fields.items():
                fields.widgets.attrs['class'] = 'form-control'
