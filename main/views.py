from django.http import HttpResponse
from .models import Movie, Person, Genre, Role
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import NewPersonForm, NewMovieForm


def main(request):
    return TemplateResponse(request, 'main.html')


def add_person(request):
    header = "Wpisz poniższe dane aby dodać osobę do bazy danych"
    if request.method == 'POST':
        form = NewPersonForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            birthdate = form.cleaned_data['birth_date']
            Person.objects.create(first_name=first_name, last_name=last_name, birthdate=birthdate)
            return TemplateResponse(request, 'person_added.html', {
                'first_name': first_name,
                'last_name': last_name,
                'header': header})
    else:
        form = NewPersonForm()
    return render(request, 'add_person_form.html', {
        'form': form,
        'header': header,
    })


def add_movie(request):
    if request.method == 'POST':
        form = NewMovieForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            director = form.cleaned_data['director']
            screenplay = form.cleaned_data['screenplay']
            release_date = form.cleaned_data['release_date']
            rating = form.cleaned_data['rating']
            genre = form.cleaned_data['genre']
            movie = Movie.objects.create(
                title=title,
                director=director,
                screenplay=screenplay,
                release_date=release_date,
                rating=rating,
            )
            movie.genre.add(genre)
            movie.save()

            return TemplateResponse(request, 'movie_added.html', {'movie': form.cleaned_data})
    else:
        form = NewMovieForm()
    return render(request, 'add_movie_form.html', {'form': form})


def show_movies(request):
    movies_in_db = Movie.objects.order_by('-release_date')
    return render(request, 'movies_table.html', {'movies_in_db': movies_in_db})


def movie_page(request):
    movie_id = request.GET['id']
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie_page.html', {'movie': movie})


def show_persons(request):
    persons_in_id = Person.objects.all()
    return render(request, 'persons_table.html', {'persons_in_db': persons_in_id})


def edit_person(request):
    header = "Wpisz poprawione dane aby edytować osobę"
    person_id = request.GET['id']
    person = Person.objects.get(pk=person_id)
    person_birthdate = person.birthdate.strftime("%d-%m-%Y")
    print(person_birthdate)
    form = NewPersonForm({
        'first_name': person.first_name,
        'last_name': person.last_name,
        'birth_date': person_birthdate,
    })
    return render(request, 'add_person_form.html', {'form': form, 'header': header})



