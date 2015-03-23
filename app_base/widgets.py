from django.forms.widgets import ChoiceInput, ChoiceFieldRenderer, RendererMixin, SelectMultiple
from django.utils.encoding import force_text
from django.utils.html import conditional_escape, format_html


class MaterializeChoiceInput(ChoiceInput):
    """
    An object used by ChoiceFieldRenderer that represents a single
    <input type='$input_type'>.
    """

    def render(self, name=None, value=None, attrs=None, choices=()):
        if self.id_for_label:
            label_for = format_html(' for="{0}"', self.id_for_label)
        else:
            label_for = ''
        return format_html('<p>{1}<label{0}>{2}</label><p>', label_for, self.tag(), self.choice_label)


class CheckboxChoiceInput(MaterializeChoiceInput):
    input_type = 'checkbox'

    def __init__(self, *args, **kwargs):
        super(CheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.value = set(force_text(v) for v in self.value)

    def is_checked(self):
        return self.choice_value in self.value


class CheckboxFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = CheckboxChoiceInput


class CheckboxSelectMultiple(RendererMixin, SelectMultiple):
    renderer = CheckboxFieldRenderer
    _empty_value = []