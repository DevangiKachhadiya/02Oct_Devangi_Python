from django import forms
from .models import *
import re 

class signupForm(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = "__all__"

# First Name Validation
    def clean_fnm(self):
        fnm = self.cleaned_data.get('fnm')
        if not re.match(r'^[A-Za-z]{2,}$', fnm):
            raise forms.ValidationError("First name must contain only alphabets and have at least 2 characters.")
        return fnm

    # Last Name Validation
    def clean_lnm(self):
        lnm = self.cleaned_data.get('lnm')
        if not re.match(r'^[A-Za-z]{2,}$', lnm):
            raise forms.ValidationError("Last name must contain only alphabets and have at least 2 characters.")
        return lnm

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise forms.ValidationError("Enter a valid email address.")
        if UserSignUp.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    # Password Validation
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
            raise forms.ValidationError("Password must be at least 8 characters long, with at least one uppercase letter, one lowercase letter, one number, and one special character.")
        return password

    # Confirm Password Validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


class addhomeForm(forms.ModelForm):
    class Meta:
        model = AddHome
        fields = ['hname', 'address', 'city', 'size', 'bedroom', 'desc', 'htype', 'sprice', 'rprice']

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
        price = cleaned_data.get('sprice')
        rprice = cleaned_data.get('rprice')

        if htype == 'sell' and not price:
            self.add_error('sprice', "Selling price is required for homes listed for sale.")
        elif htype == 'rent' and not rprice:
            self.add_error('rprice', "Rent price is required for homes listed for rent.")
        return cleaned_data


class homeimageForm(forms.ModelForm):
    class Meta:
        model = HomeImage
        fields = ['image']

class contactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class apply_ownerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'email', 'number']

