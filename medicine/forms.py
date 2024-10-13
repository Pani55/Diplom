from django.forms import ModelForm, BooleanField
from medicine.models import Feedback, Appointment


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class FeedbackForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Feedback
        fields = ["text"]


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "procedure", "appointment_datetime"]
