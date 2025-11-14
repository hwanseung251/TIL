from rest_framework import serializers
from .models import Actor, Movie, Review


# ---- Actor 관련 ----
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name')


class ActorDetailSerializer(serializers.ModelSerializer):

    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')
            
    # Actor.movies (ManyToMany) 를 통해 출연 영화 목록
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')


# ---- Movie 관련 ----
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'overview')


class MovieDetailSerializer(serializers.ModelSerializer):

    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('id', 'name')


    class ReviewSimpleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('id', 'title', 'content')
            
    actors = ActorNameSerializer(many=True, read_only=True)
    reviews = ReviewSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'overview',
            'release_date',
            'poster_path',
            'actors',
            'reviews',
        )


# ---- Review 관련 ----
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title', 'content')


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'movie_title')


class ReviewCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')
