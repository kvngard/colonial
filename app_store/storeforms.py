from django import forms
import app_base.models as mod
import requests


class Address_Form(forms.ModelForm):

    class Meta:
        model = mod.Address


class Credit_Card_Form(forms.Form):
    def __init__(self, *args, **kwargs):
        self.total = kwargs.pop('total', None)
        self.user = kwargs.pop('user', None)
        self.resp = None
        super(Credit_Card_Form, self).__init__(*args, **kwargs)

    name = forms.CharField(label='Name On Card', max_length=100)
    cc_type = forms.CharField(label='Card Type', max_length=30)
    number = forms.CharField(label='Card Number', max_length=30)
    cvc = forms.CharField(label='CVC', max_length=3)
    exp_date = forms.CharField(label='Exp Date', max_length=7)

    def clean(self):
        print(self.total, self.user)

        API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
        API_KEY = '79b9af41b515bad70956159f111050e6'

        card_type = self.cleaned_data.get('cc_type')
        card_number = self.cleaned_data.get('number')
        cvc = self.cleaned_data.get('cvc')
        exp_month = self.cleaned_data.get('exp_date').split('/')[0]
        exp_year = self.cleaned_data.get('exp_date').split('/')[1]
        full_name = self.cleaned_data.get('name')

        r = requests.post(API_URL, data={
                'apiKey': API_KEY,
                'currency': 'usd',
                'amount': self.total,
                'type': card_type,
                'number': card_number,
                'exp_month': exp_month,
                'exp_year': exp_year,
                'cvc': cvc,
                'name': full_name,
                'description': 'Charge for {}.'.format(self.user.email)
            })

        resp = r.json()

        if 'error' in resp:
            raise forms.ValidationError(resp['error'])
        else:
            print(resp.keys())
            self.resp = resp
