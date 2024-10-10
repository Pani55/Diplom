from django.forms import ModelForm
from medicine.models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["text"]
