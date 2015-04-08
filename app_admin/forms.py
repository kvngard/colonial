from app_base.widgets import CheckboxSelectMultiple
from app_base.forms import site_model_form
from app_base.models import User, Event


class ManagerUserEditForm(site_model_form):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }


class EventEditForm(site_model_form):

    class Meta:
        model = Event
        fields = ['start_date', 'end_date', 'venue_name', 'map_file_name', 'address', 'discount_code']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }