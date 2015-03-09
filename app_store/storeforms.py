from django import forms
import app_base.models as mod


class CheckoutForm(forms.ModelForm):
    credit = forms.CharField(label='Credit Card', max_length=100)

    class Meta:
        model = mod.Address
