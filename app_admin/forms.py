from app_base.widgets import CheckboxSelectMultiple
from app_base.forms import site_model_form
from app_base.models import User


class ManagerUserEditForm(site_model_form):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups']
        widgets = {
            'groups': CheckboxSelectMultiple(),
        }
