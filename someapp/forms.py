from django.forms import ModelForm
from .models import Request, Feedback

class RequestForm(ModelForm):
    class Meta:
        model = Request
        exclude = ['status']

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'