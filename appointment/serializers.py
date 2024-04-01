from rest_framework import serializers
from . import models

# serializer er kaz hosse python er model k json a convirt kore dibe jate ai api mobile phone, dekstop, web app jokono jaygay jate ai api use kora jay. 
class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.StringRelatedField(many=False) #aktai time select korte parbe
    patient = serializers.StringRelatedField(many=False)
    doctor = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Appointment
        fields = '__all__'
