from app_base.widgets import CheckboxSelectMultiple, MaterializeClearableFileInput
from app_base.models import User, Event, Area, Item, Sale_Item, Rental_Item, Custom_Item
from app_base.forms import site_model_form
from app_base.widgets import RadioSelect
import app_base.models as mod
from django import forms

'''
    classes for creating forms
'''


class Return_Form(forms.ModelForm):

    class Meta:
        model = mod.Rental_Return
        fields = ['return_condition']
        widgets = {
            'return_condition': RadioSelect(),
        }


class Damage_Form(forms.ModelForm):

    class Meta:
        model = mod.Damage_Fee
        fields = ['description', 'amount']


class ManagerUserEditForm(site_model_form):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }


class EventEditForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['name', 'description', 'start_date', 'end_date', 'venue_name',
                  'map_file', 'address', 'discount_code']
        widgets = {
            'map_file': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }


class AreaEditForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['name', 'description', 'coordinator',
                  'supervisor', 'place_number']


class ItemEditForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'description', 'serial_number',
                  'value', 'owner', 'photo']
        widgets = {
            'photo': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }


class SaleItemEditForm(forms.ModelForm):

    class Meta:
        model = Sale_Item
        fields = ['name', 'description', 'value', 'owner',
                  'quantity_on_hand', 'photo', 'price', 'manufacturer', 'creator']
        widgets = {
            'photo': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }


class RentalItemEditForm(forms.ModelForm):

    class Meta:
        model = Rental_Item
        fields = ['name', 'description', 'value', 'owner',
                  'quantity_on_hand', 'photo', 'price_per_day']
        widgets = {
            'photo': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }


class CustomItemEditForm(forms.ModelForm):

    class Meta:
        model = Custom_Item
        fields = ['name', 'description', 'value', 'owner',
                  'photo', 'production_time', 'required_info']
        widgets = {
            'photo': MaterializeClearableFileInput(attrs={'class': 'upload-btn'}),
        }
