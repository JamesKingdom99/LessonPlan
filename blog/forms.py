from django import forms
from tinymce import TinyMCE
from .models import PostForms


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class lessonPlan(forms.ModelForm):
    perfTask = forms.CharField(
        widget=TinyMCEWidget(
            mce_attrs={'width': 800}
        ),
    )
    background = forms.CharField(
        widget=TinyMCEWidget(
            mce_attrs={'width': 800}
        ),
    )
    title = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'What is on your lesson about?'}
        ),
    )
    ls = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'What is on your lesson learning target?'}
        ),
    )
    question = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'What is on your guiding question?'}
        ),
    )
    presentation = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Insert presentation link here.'}
        ),
    )
    quiz = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Insert assessment link here.'}
        ),
    )
    vocab = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Insert quizlet link here.'}
        ),
    )
    wiki = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 1, 'placeholder': 'Insert wiki link here.'}
        ),
    )

    class Meta:
        model = PostForms
        fields = ['title','ls', 'question', 'presentation', 'background',
        'perfTask', 'quiz', 'vocab', 'wiki']
