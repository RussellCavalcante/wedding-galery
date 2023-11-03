from django.forms.models import BaseInlineFormSet


class ComentarioObrigatorio(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(ComentarioObrigatorio, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form
