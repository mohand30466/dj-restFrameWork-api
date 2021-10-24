from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieVeiwSet, RatesVeiwSet,  UserVeiwSet


router = routers.DefaultRouter()
router.register('movies', MovieVeiwSet)
router.register('Rates', RatesVeiwSet)
router.register('users', UserVeiwSet)


urlpatterns = [
    path('', include(router.urls)),
]