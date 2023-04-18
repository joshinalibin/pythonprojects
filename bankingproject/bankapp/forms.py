from django import forms
from .models import Details,District,Branch


class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(max_length=250)
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], widget=forms.RadioSelect)
    account_type = forms.ChoiceField(choices=Details.ACCOUNT_TYPES)

    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label="Select District")
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), empty_label="Select Branch")
    MATERIAL_CHOICES = (

        ('Debit card', 'Debit card'),
        ('Credit card', 'Credit card'),
        ('Cheque Book', 'Cheque Book'),
    )
    materials_required = forms.MultipleChoiceField(choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Details
        fields = ['district', 'branch', 'dob', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(distid_id=district_id).order_by('distid')
            except (ValueError, TypeError):
                pass

