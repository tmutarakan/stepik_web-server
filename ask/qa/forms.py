from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        return Question.objects.create(**self.cleaned_data)


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.ModelChoiceField(queryset=Question.objects.all())

    def clean(self):
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author'] = self._user
        Answer.objects.create(**self.cleaned_data)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    password = forms.CharField(max_length=256, widget=forms.PasswordInput())

    def save(self):
        return User.objects.create(**self.cleaned_data)
