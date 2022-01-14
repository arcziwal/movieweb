from django import forms
from .models import Person, Genre


class NewPersonForm(forms.Form):
    first_name = forms.CharField(label='Imię', max_length=32)
    last_name = forms.CharField(label="Nazwisko", max_length=32)
    birth_date = forms.DateField(label="Data urodzenia", error_messages={'invalid': """Błędna data!
    Podaj datę w formacie DD-MM-RRRR!
    """}, input_formats=['%d-%m-%Y'])


class NewMovieForm(forms.Form):
    title = forms.CharField(label='Tytuł', max_length=120)
    director = forms.ModelChoiceField(queryset=Person.objects.all(), label='Reżyser')
    screenplay = forms.ModelChoiceField(queryset=Person.objects.all(), label="Scenariusz")
    release_date = forms.DateField(label="Data premiery", input_formats=["%d-%m-%Y"], error_messages={'invalid': """
    Błędna data! POdaj datę w formacie DD-MM-RRRR!
    """})
    rating = forms.FloatField(required=None, min_value=0.0, max_value=10.0, label="Ocena", help_text="Od 0.0 do 10.0")
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), label="Gatunek")
    img = forms.ImageField(label="Okładka", required=False)




