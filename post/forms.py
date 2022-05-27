from django.forms import ModelForm, Textarea
from . models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'more_information': Textarea(attrs={'id': 'more-information-field'})
        }