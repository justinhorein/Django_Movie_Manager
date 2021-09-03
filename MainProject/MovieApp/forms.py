from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'id':'pk',
            'title':'Title',
            'director':'Director',
            'studio':'Studio',
            'platform':'Platform',
            'year':'Year',
        }
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }


