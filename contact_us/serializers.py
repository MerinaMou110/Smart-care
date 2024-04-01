from rest_framework import serializers
from . import models

# model er data gulo serializer er madhome jvscript er json a convirt hoa jabe. json hsse backend er shate frontend er communication media
# json k convirt korar process k bole serialization
# ai serialization er kaz j kore take bole serializer
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = '__all__'