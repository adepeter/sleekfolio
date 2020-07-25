from django import forms

class BooleanRadioYesNo(forms.BooleanField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = forms.RadioSelect()