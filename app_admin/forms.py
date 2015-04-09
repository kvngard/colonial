from app_base.widgets import CheckboxSelectMultiple, MaterializeClearableFileInput
from app_base.forms import site_model_form
from app_base.models import User, Event
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
