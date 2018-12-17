from django import forms
from . models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields =['text']
        widgets = {'text':forms.Textarea()}
