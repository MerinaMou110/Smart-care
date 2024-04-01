from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter() # wifi toiri korlam
# shob dhoroner req handle korbe antena
router.register('', views.AppointmentViewSet) # ekta entena toiri korlam

urlpatterns = [
    path('', include(router.urls)),
]

