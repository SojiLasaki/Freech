from django.forms import ModelForm
from .models import *

class ConvoForm(ModelForm):
    class Meta:
        model = Convo
        fields = ['title', 'body']
        
    def __init__(self, *args, **kwargs):
        super(ConvoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input', 'placeholder': field.label})


class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(ConvoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input', 'placeholder': field.label})

    
class CircleForm(ModelForm):
    class Meta:
        model = Circle
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CircleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
                field.widget.attrs.update({'class': 'input', 'placeholder': field.label})


# class FlashcardForm(ModelForm):
#     class Meta:
#         model = Flashcard
#         fields = ['question', 'answer',]
    
#     def __init__(self, *args, **kwargs):
#         super(FlashcardForm, self).__init__(*args, **kwargs)

#         for name, field in self.fields.items():
#                 field.widget.attrs.update({'class': 'input', 'placeholder': field.label})