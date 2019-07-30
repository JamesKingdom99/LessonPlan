from django import forms
from tinymce import TinyMCE
from .models import Post, Topic, Board

class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=TinyMCEWidget(
            mce_attrs={'width': 800}
        ),
    )

    class Meta:
        model = Topic
        fields = ['subject']



class PostForm(forms.ModelForm):
    message = forms.CharField(
        widget=TinyMCEWidget(
            mce_attrs={'width': 800}
        )
    )

    class Meta:
        model = Post
        fields = ['message']


class NewBoard(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )



    class Meta:
        model = Board
        fields = ['name', 'description']
