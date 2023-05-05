from django import forms
from .models import Contact, Booking


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','subject','message']

    def __init__(self,*args,**kwargs): 
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter Your Name', 
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
        self.fields['subject'].widget.attrs['placeholder'] = 'Enter Your Subject'
        self.fields['message'].widget.attrs={'placeholder' : 'Enter Your Message','rows' : 5}
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control' 



class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','email','check_in','check_out','num_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'check_in': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check-in date','type':'date'}),
            'check_out': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check-out date','type':'date'}),
            'num_of_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of guests'})
        }
