
from rest_framework import viewsets, status
from .models import Movies, Rates
from .serializers import MoviesSerializer, RatesSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication



class UserVeiwSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
 
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, )
  

class MovieVeiwSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer 
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated , AllowAny)
    # authenticators=self.get_authenticators(),
   

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
       
        if 'stars' in request.data:
             movie = Movies.objects.get(id=pk)
             stars = request.data['stars']
             user = request.user
             print("user", user)


             try:
                rating = Rates.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                serializers = RatesSerializer(rating, many=False)
                response = {'message': 'its updating', 'result': serializers.data}
                return Response(response, status=200)


             except:

                 rating = Rates.objects.create(user=user, movie=movie, stars=stars)

                 serializers = RatesSerializer(rating, many= False)

                 response = {'message':'its working', 'result': serializers.data}

                 return Response(response, status=200)

        else:
            response = {'message': 'its not working you miss to enter date'}
            return Response(response, status=500)

    
 

class RatesVeiwSet(viewsets.ModelViewSet):
    queryset = Rates.objects.all()
    serializer_class = RatesSerializer
    authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated)

    def create(self, request, *args, **kwargs):
        res = {'messages': "you cant create rating like that"}
        return Response(res, status=404)

    def update(self, request, *args, **kwargs):
        res = {'messages': "you cant update rating like that"}
        return Response(res, status=404)
