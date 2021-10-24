from rest_framework import serializers
from .models import Movies, Rates
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import UserProfile




class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=40)
    password = serializers.CharField(max_length=40, min_length=6, write_only=True, required=True)
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email = serializers.CharField(max_length=244, min_length=6, required=True)



    class Meta:
        model = User

        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email')





    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.address = serializers.CharField(max_length=40)
        Token.objects.create(user=user)
        return user


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('id', 'title', 'discription', 'num_of_rating', 'average_of_rating')

class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ('id', 'user', 'movie', 'stars')


class UserProSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('address', 'country', 'profissional', 'profilebic', 'telephone')
