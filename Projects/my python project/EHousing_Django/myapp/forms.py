from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model = userSignup
        fields = "__all__"

class addhomeForm(forms.ModelForm):
    class Meta:
        model = addhome
        fields = ['hname', 'address', 'city', 'size', 'bedroom', 'desc', 'htype', 'price', 'rprice']

class HomeImageForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = ['image']

 # Validation for Home Name
    def clean_hname(self):
        hname = self.cleaned_data.get('hname')
        if len(hname) < 3:
            raise forms.ValidationError("Home name must be at least 3 characters long.")
        return hname

    # Validation for Address
    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 5:
            raise forms.ValidationError("Address must be at least 5 characters long.")
        return address

    # Validation for City
    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city.isalpha():
            raise forms.ValidationError("City name should only contain letters.")
        return city

    # Validation for Size
    def clean_size(self):
        size = self.cleaned_data.get('size')
        if size <= 0:
            raise forms.ValidationError("Size must be greater than 0.")
        return size

    # Validation for Bedrooms
    def clean_bedroom(self):
        bedroom = self.cleaned_data.get('bedroom')
        if bedroom <= 0:
            raise forms.ValidationError("There must be at least 1 bedroom.")
        return bedroom

    # Conditional Validation for Rent and Sell
    def clean(self):
        cleaned_data = super().clean()
        htype = cleaned_data.get('htype')
        price = cleaned_data.get('price')
        rprice = cleaned_data.get('rprice')

        if htype == 'sell' and not price:
            self.add_error('price', "Selling price is required for homes listed for sale.")
        elif htype == 'rent' and not rprice:
            self.add_error('rprice', "Rent price is required for homes listed for rent.")
        return cleaned_data

