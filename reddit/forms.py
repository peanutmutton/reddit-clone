from django import forms

class SubmitPostForm(forms.Form):
    title = forms.CharField(max_length=30)
    subreddit = forms.CharField(max_length=30)
    body = forms.CharField(widget=forms.Textarea)
