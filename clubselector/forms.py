from django import forms

class QuizResponseForm(forms.Form):
    question1 = forms.IntegerField(min_value=1, max_value=10)
    question2 = forms.IntegerField(min_value=1, max_value=10)