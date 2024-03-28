from django import forms
from datetime import datetime

class Employee(forms.Form):
    EMPLOYEE_IDS = (
        ('1','Employee 1'),
        ('2','Employee 2'),
        ('3','Employee 3')
    )

    employee_id = forms.ChoiceField(choices=EMPLOYEE_IDS,label='Select your Employee ID')
    date_of_joining = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date'}))
