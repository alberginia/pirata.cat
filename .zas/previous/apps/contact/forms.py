from apps.contact.models import Message, Interested
from django.forms import ModelForm


class MessageForm(ModelForm):

    class Meta:
        model = Message


class InterestedForm(ModelForm):

    class Meta:
        model = Interested
        fields = ("email", )


