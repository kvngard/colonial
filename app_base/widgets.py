from django.forms.widgets import ChoiceInput, ChoiceFieldRenderer, RendererMixin, SelectMultiple, Select, ClearableFileInput, CheckboxInput
from django.utils.html import conditional_escape, format_html
from django.utils.safestring import mark_safe
from django.utils.encoding import force_text


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


class MaterializeRadioChoiceInput(MaterializeChoiceInput):
    input_type = 'radio'

    def __init__(self, *args, **kwargs):
        super(MaterializeRadioChoiceInput, self).__init__(*args, **kwargs)
        self.value = force_text(self.value)


class MaterializeCheckboxChoiceInput(MaterializeChoiceInput):
    input_type = 'checkbox'

    def __init__(self, *args, **kwargs):
        super(MaterializeCheckboxChoiceInput, self).__init__(*args, **kwargs)
        self.value = set(force_text(v) for v in self.value)

    def is_checked(self):
        return self.choice_value in self.value


class ChoiceFieldRenderer(object):

    """
    An object used by RadioSelect to enable customization of radio widgets.
    """

    choice_input_class = None

    def __init__(self, name, value, attrs, choices):
        self.name = name
        self.value = value
        self.attrs = attrs
        self.choices = choices

    def __getitem__(self, idx):
        choice = self.choices[idx]  # Let the IndexError propagate
        return self.choice_input_class(self.name, self.value, self.attrs.copy(), choice, idx)

    def __str__(self):
        return self.render()

    def render(self):
        """
        Outputs a <ul> for this set of choice fields.
        If an id was given to the field, it is applied to the <ul> (each
        item in the list will get an id of `$id_$i`).
        """
        id_ = self.attrs.get('id', None)
        start_tag = format_html('<ul id="{0}">', id_) if id_ else '<ul>'
        output = [start_tag]
        for i, choice in enumerate(self.choices):
            choice_value, choice_label = choice
            if isinstance(choice_label, (tuple, list)):
                attrs_plus = self.attrs.copy()
                if id_:
                    attrs_plus['id'] += '_{0}'.format(i)
                sub_ul_renderer = ChoiceFieldRenderer(name=self.name,
                                                      value=self.value,
                                                      attrs=attrs_plus,
                                                      choices=choice_label)
                sub_ul_renderer.choice_input_class = self.choice_input_class
                output.append(format_html('<li>{0}{1}</li>', choice_value,
                                          sub_ul_renderer.render()))
            else:
                w = self.choice_input_class(self.name, self.value,
                                            self.attrs.copy(), choice, i)
                output.append(format_html('<li>{0}</li>', force_text(w)))
        output.append('</ul>')
        return mark_safe('\n'.join(output))


class RadioFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = MaterializeRadioChoiceInput


class CheckboxFieldRenderer(ChoiceFieldRenderer):
    choice_input_class = MaterializeCheckboxChoiceInput

    def render(self):
        """
        Outputs a <ul> for this set of choice fields.
        If an id was given to the field, it is applied to the <ul> (each
        item in the list will get an id of `$id_$i`).
        """
        id_ = self.attrs.get('id', None)
        start_tag = format_html(
            '<ul id="{0}"><br />', id_) if id_ else '<ul><br />'
        output = [start_tag]
        for i, choice in enumerate(self.choices):
            choice_value, choice_label = choice
            if isinstance(choice_label, (tuple, list)):
                attrs_plus = self.attrs.copy()
                if id_:
                    attrs_plus['id'] += '_{0}'.format(i)
                sub_ul_renderer = ChoiceFieldRenderer(name=self.name,
                                                      value=self.value,
                                                      attrs=attrs_plus,
                                                      choices=choice_label)
                sub_ul_renderer.choice_input_class = self.choice_input_class
                output.append(format_html('<li>{0}{1}</li>', choice_value,
                                          sub_ul_renderer.render()))
            else:
                w = self.choice_input_class(self.name, self.value,
                                            self.attrs.copy(), choice, i)
                output.append(format_html('<li>{0}</li>', force_text(w)))
        output.append('</ul>')
        return mark_safe('\n'.join(output))


class RadioSelect(RendererMixin, Select):
    renderer = RadioFieldRenderer
    _empty_value = ''


class CheckboxSelectMultiple(RendererMixin, SelectMultiple):
    renderer = CheckboxFieldRenderer
    _empty_value = []


class MaterializeClearableFileInput(ClearableFileInput):

    def render(self, name, value, attrs=None):
        substitutions = {
            'input_text': self.input_text,
        }
        template = '''<div class="file-field input-field"><input class="file-path validate"
        type="text"/><div class="btn"><span>File</span>%(input)s</div></div>'''
        substitutions['input'] = super(
            ClearableFileInput, self).render(name, value, attrs)

        return mark_safe(template % substitutions)
