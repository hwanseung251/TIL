# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Actor, Movie, Review
from .serializers import (
    ActorListSerializer,
    ActorDetailSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    ReviewListSerializer,
    ReviewDetailSerializer,
    ReviewCreateUpdateSerializer,
)


# ===== Actor =====

@api_view(['GET'])
def actor_list(request):
    """
    F06. 전체 배우 목록 조회
    GET /api/v1/actors/
    """
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    """
    F07. 특정 배우 정보 + 출연 영화 조회
    GET /api/v1/actors/<actor_pk>/
    """
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)


# ===== Movie =====

@api_view(['GET'])
def movie_list(request):
    """
    F08. 전체 영화 목록 조회
    GET /api/v1/movies/
    """
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    """
    F09. 특정 영화 정보 + 배우 목록 + 리뷰 목록 조회
    GET /api/v1/movies/<movie_pk>/
    """
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


# ===== Review =====

@api_view(['GET'])
def review_list(request):
    """
    F10. 전체 리뷰 목록 조회
    GET /api/v1/reviews/
    """
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    """
    F11. 리뷰 단일 조회 / 수정 / 삭제
    - GET    /api/v1/reviews/<review_pk>/
    - PUT    /api/v1/reviews/<review_pk>/
    - DELETE /api/v1/reviews/<review_pk>/
    """
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewCreateUpdateSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            detail_serializer = ReviewDetailSerializer(review)
            return Response(detail_serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request, movie_pk):
    """
    F12. 특정 영화에 대한 리뷰 생성
    POST /api/v1/movies/<movie_pk>/reviews/
    body: { "title": "...", "content": "..." }
    """
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = ReviewCreateUpdateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        review = serializer.save(movie=movie)
        detail_serializer = ReviewDetailSerializer(review)
        return Response(detail_serializer.data, status=status.HTTP_201_CREATED)