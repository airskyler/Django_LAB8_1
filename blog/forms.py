

from django import forms

from .models import Post


# the word "PostForm" is a name of the form and 
# it is telling Django that this form is a ModelForm
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
		
		# The form will inculed the title and text
        fields = ('title', 'text',)

		