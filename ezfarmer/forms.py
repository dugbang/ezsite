from django.forms import ModelForm

from ezfarmer.models import Capture


class CaptureForm(ModelForm):
    class Meta:
        model = Capture
        fields = ('plant', 'name', 'image', 'create_date')

