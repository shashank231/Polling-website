from.models import *
from django.forms import ModelForm

class CreatepollForm(ModelForm):
    class Meta:
        model = Createpoll
        fields = '__all__'
        exclude = ['vo1', 'vo2', 'vo3']
