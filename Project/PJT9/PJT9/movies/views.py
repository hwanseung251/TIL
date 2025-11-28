from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_safe
from .models import Movie, Genre

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movies/index.html', context)


def filter_genre(request):
    genre_id = request.GET.get('genre_id')

    if genre_id == 'all' or not genre_id:
        movies = Movie.objects.all()
    else:
        movies = Movie.objects.filter(genres__id=genre_id)

    # JSON 응답
    movies_data = []
    for movie in movies:
        movies_data.append({
            'title': movie.title,
        })

    return JsonResponse({'movies': movies_data})

@require_safe
def recommended(request):
    pass
