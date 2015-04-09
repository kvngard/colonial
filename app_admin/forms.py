from app_base.widgets import CheckboxSelectMultiple, MaterializeClearableFileInput
from app_base.forms import site_model_form
from app_base.models import User, Event, Area, Item
from django import forms


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
        fields = ['start_date', 'end_date', 'venue_name',
                  'map_file', 'address', 'discount_code']


class AreaEditForm(forms.ModelForm):

    class Meta:
        model = Area
        fields = ['name', 'description', 'coordinator',
                  'supervisor', 'place_number']


class ItemEditForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['name', 'description', 'serial_number',
                  'value', 'owner', 'photo', 'clothing_detail']