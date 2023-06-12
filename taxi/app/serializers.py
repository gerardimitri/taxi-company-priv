from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
import math

from .models import (
    Client,
    Driver,
    Route,
    Trip,
    BackgroundCheck,
    ClientPayment,
    DriverPayment,
    RideChat,
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "first_name",
            "last_name",
            "email",
            "associated_card_number",
            "associated_card_type",
            "score",
        ]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            "first_name",
            "last_name",
            "email",
            "rut",
            "bank",
            "bank_account_number",
            "car_plate",
            "car_brand",
            "car_model",
            "car_color",
            "score",
        ]


class TripSerializer(serializers.ModelSerializer):
    trip_routes = SerializerMethodField()

    class Meta:
        model = Trip
        fields = [
            "client",
            "driver",
            "cost",
            "created_at",
            "payment",
            "completion_state",
            "score",
            "trip_routes",
        ]

    def get_trip_routes(self, trip):
        trip_routes = Route.objects.filter(trip=trip.id)
        serializer = RouteNoTripSerializer(trip_routes, many=True)
        return serializer.data


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ["lat_coord", "lon_coord", "timestamp", "trip"]


class RouteNoTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ["lat_coord", "lon_coord", "timestamp"]


class BackgroundCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundCheck
        fields = [
            "driver",
            "age",
            "criminal_record",
            "profile_headshot",
            "id_photo",
            "status_of_procedure",
        ]


class ClientPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPayment
        fields = [
            "client",
            "created_at",
            "trip",
            "amount",
            "payment_method",
            "status",
        ]

    def create(self, validated_data):
        obj = ClientPayment.objects.create(**validated_data)
        trip = validated_data["trip"]
        obj.amount = math.ceil(trip.cost * 1.1)
        obj.payment_method = trip.payment
        obj.save()
        return obj


class DriverPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverPayment
        fields = [
            "driver",
            "created_at",
            "trip",
            "amount",
            "bank",
            "bank_account_number",
            "status",
        ]

    def create(self, validated_data):
        obj = DriverPayment.objects.create(**validated_data)
        trip = validated_data["trip"]
        driver = validated_data["driver"]
        obj.amount = math.ceil(trip.cost * 1.1)
        obj.bank = driver.bank
        obj.bank_account_number = driver.bank_account_number
        obj.save()
        return obj


class RideChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideChat
        fields = [
            "driver",
            "client",
            "created_at",
            "trip",
            "chat",
        ]
