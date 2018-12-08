from django.forms import ModelForm


class ShortenerForm(ModelForm):
    class Meta:
        fields = ['url']
