from django import forms
from .models import PaymentDetails
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            'name',
            'amount',
            Submit('submit', 'Donate', css_class='button white btn-block btn-primary')
        )
