from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('', views.ServiceViewset) # router er antena.protita views er jnnno akti antena
urlpatterns = [
    path('', include(router.urls)),
]