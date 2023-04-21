from rest_framework import serializers
from .models import Actor, Movie, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

        read_only_fields = ('movie',)

class ReviewlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

        # read_only_fields = ('movie_id',)

class ReviewdetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_movie(self, review):

        movie = review.movie

        return [{"title" : movie.title}]


class MovieslistSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only = True)
    
    class Meta:
        model = Movie
        fields = ('title', 'overview')

class MoviesdetailSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    # reviews = ReviewSerializer(many=True, read_only = True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_actors(self, movie):
        actors = movie.actors.all()
        return [{"name" : actor.name} for actor in actors]
    
    def get_reviews(self, movie):
        reviews = movie.reviews.all()
        return [{"title" : review.title, "content" : review.content} for review in reviews]


class ActorMovieSerializer(serializers.ModelSerializer):
    # title_and_overview = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = ('title',)



class ActorslistSerializer(serializers.ModelSerializer):
    # movies = serializers.SerializerMethodField()
    
    class Meta:
        model = Actor
        fields = '__all__'

    # def get_movies(self, actor):
    #     movies = actor.movie_set.all()
    #     return [{"title" : movie.title} for movie in movies]

class ActorsdetailSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()
    
    class Meta:
        model = Actor
        fields = '__all__'

    def get_movies(self, actor):
        movies = actor.movie_set.all()
        return [{"title" : movie.title} for movie in movies]