from django import forms 

class Student(forms.Form):
    name = forms.CharField(label='Name',max_length=100)
    date_of_birth = forms.DateField(label='Date of birth',widget=forms.widgets.DateInput(attrs={'type':'date'}))
    address = forms.CharField(label='Address',widget=forms.Textarea)
    contact_number = forms.CharField(label='Contact Number', max_length=15)
    email_id = forms.EmailField(label='Email id')
    marks_english = forms.IntegerField(label='Marks in English')
    marks_physics = forms.IntegerField(label='Marks in Physics')
    marks_chemistry = forms.IntegerField(label='Marks in Chemistry')