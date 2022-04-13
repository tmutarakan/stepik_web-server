from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def clean(self):
        # text = self.cleaned_data['text']
        # if not text.is_valid():
        #     raise forms.ValidationError('question text is wrong', code=12)
        return self.cleaned_data

    def save(self):
        Answer.objects.create(**self.cleaned_data)
