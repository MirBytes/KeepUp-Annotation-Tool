from django import forms
from .models import PostFeatures, Comments

class PostFeaturesForm(forms.ModelForm):

    OPTIONS = [
            ('None', '-- Select --'),
            ('0', 'Real'),
            ('1', 'Fake'),
        ]
    annotatorOne_post_label = forms.ChoiceField(
        choices=OPTIONS, 
         widget=forms.Select(attrs={'class': 'form-control'}),
         label="Your Label:",
         required=False
    )

    annotatorTwo_post_label =  forms.ChoiceField(
        choices=OPTIONS, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Your Label:",
        required=False
    )

    annotatorThree_post_label = forms.ChoiceField(
        choices=OPTIONS, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Your Label:",
        required=False
    )

    class Meta:
       
        model = PostFeatures
        fields = ['post_title', 'likescount', 'commentscount', 'views', 'shares', 'reposts', 'post_label', 'platform', 'post_url', 'annotatorOne_post_label', 
                  'annotatorTwo_post_label', 'annotatorThree_post_label']
        

        
        widgets = {
            'post_title': forms.Textarea(attrs={'rows': 4, 'cols': 170, 'class': 'form-control'})
        }

       
        labels = {
             'post_label' : "Student's Label:"
        }

    def __init__(self, *args, **kwargs):
            super(PostFeaturesForm, self).__init__(*args, **kwargs)
            
            self.fields['likescount'].widget.attrs.update({'class': 'form-control'})
            self.fields['commentscount'].widget.attrs.update({'class': 'form-control'})
            self.fields['post_label'].widget.attrs.update({'class': 'form-control'})
            self.fields['views'].widget.attrs.update({'class': 'form-control'})
            self.fields['shares'].widget.attrs.update({'class': 'form-control'})
            self.fields['reposts'].widget.attrs.update({'class': 'form-control'})

            # set these fields read-only
            for field in ['post_label', 'views', 'shares', 'reposts']:
                self.fields[field].disabled = True  


class CommentsForm(forms.ModelForm):

    OPTIONS = [
            ('None', '-- Select --'),
            ('agree', 'Agree'),
            ('disagree', 'Disagree'),
            ('query', 'Query'),
            ('comment', 'Comment')
        ]
    
    annotatorOne_comment_label = forms.ChoiceField(
        choices=OPTIONS, 
         widget=forms.Select(attrs={'class': 'form-control'}),
         label="Your Label:",
         required=False
    )

    annotatorTwo_comment_label =  forms.ChoiceField(
        choices=OPTIONS, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Your Label:",
        required=False
    )

    annotatorThree_comment_label = forms.ChoiceField(
        choices=OPTIONS, 
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Your Label:",
        required=False
    )
    class Meta:
       
        model = Comments
        fields = ['commenttext', 'comment_label', 'label', 'annotatorOne_comment_label', 
                  'annotatorTwo_comment_label', 'annotatorThree_comment_label']
        
        widgets = {
            'commenttext': forms.Textarea(attrs={'rows': 4, 'cols': 170, 'class': 'form-control'})
        }
       
        labels = {
             'comment_label' : "Student's Label:"
        }

    def __init__(self, *args, **kwargs):
            super(CommentsForm, self).__init__(*args, **kwargs)
            
            self.fields['commenttext'].widget.attrs.update({'class': 'form-control'})
            self.fields['comment_label'].widget.attrs.update({'class': 'form-control'})
            self.fields['label'].widget.attrs.update({'class': 'form-control'})

            # set these fields read-only
            for field in ['comment_label', 'label']:
                self.fields[field].disabled = True  