from django import forms


class searchforms(forms.Form):
    searchfield = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['searchfield'].widget.attrs.update(
            {"class": "form-control"})
