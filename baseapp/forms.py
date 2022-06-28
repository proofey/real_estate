from django import forms
from django.contrib.auth.forms import AuthenticationForm
from post.models import PropertyType, OfferType


class LoginForm(AuthenticationForm):
    fields = ['username', 'password']


class SearchForm(forms.Form):
    property_choices = PropertyType.objects.all()
    offer_coices = OfferType.objects.all()

    property_type = forms.ModelChoiceField(property_choices, label='Property')
    offer_type = forms.ModelChoiceField(offer_coices, label='Offer')
    location = forms.CharField(max_length=50, label='Location',
                               required=False,
                               widget=forms.TextInput(attrs={'placeholder': "Enter location..."}))
    minimum_price = forms.IntegerField(required=False, 
                                       widget=forms.TextInput(attrs={'placeholder': 'Enter price...'}))
    maximum_price = forms.IntegerField(required=False, 
                                       widget=forms.TextInput(attrs={'placeholder': 'Enter price...'}))


  