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

from .serializers import (
    ClientSerializer,
    DriverSerializer,
    RouteSerializer,
    TripSerializer,
    BackgroundCheckSerializer,
    ClientPaymentSerializer,
    DriverPaymentSerializer,
    RideChatSerializer,
)
from rest_framework import mixins
from rest_framework import generics


# import random
# from rest_framework.decorators import api_view

# --- examples ---

# @api_view(["GET", "POST"])
# def index(request):
#     """
#     Displays a random integer between 0 and 100, or returns the div of a random
#     number between 0 and 100 by a given integer.
#     """
#     if request.method == "GET":
#         random_integer = random.randrange(101)
#         dict = {"random integer value": random_integer}
#         return Response(dict)

#     elif request.method == "POST":
#         input_integer = int(request.data["value"])
#         random_integer = random.randrange(101)
#         if input_integer == 0:
#             dict = {
#                 "random integer to divide": random_integer,
#                 "input integer": input_integer,
#                 "Error": "cannot divide a number by zero.",
#             }
#             return Response(dict, status=status.HTTP_400_BAD_REQUEST)
#         div = random_integer // input_integer
#         dict = {
#             "random integer to divide": random_integer,
#             "input integer": input_integer,
#             "floor division value": div,
#         }
#         return Response(dict, status=status.HTTP_200_OK)

# --- project ---

# Trip views


class TripListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TripDetailApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Cient views


class ClientListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ClientDetailApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Driver views


class DriverListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DriverDetailApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Route views


class RouteListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RouteDetailApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Background Check views


class BackgroundCheckListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = BackgroundCheck.objects.all()
    serializer_class = BackgroundCheckSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BackgroundCheckDetailApiView(
    mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = BackgroundCheck.objects.all()
    serializer_class = BackgroundCheckSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Client Payment views


class ClientPaymentListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = ClientPayment.objects.all()
    serializer_class = ClientPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ClientPaymentDetailApiView(
    mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = ClientPayment.objects.all()
    serializer_class = ClientPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Driver Payment views


class DriverPaymentListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DriverPaymentDetailApiView(
    mixins.RetrieveModelMixin, generics.GenericAPIView
):
    queryset = DriverPayment.objects.all()
    serializer_class = DriverPaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# RideChat views


class RideChatListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = RideChat.objects.all()
    serializer_class = RideChatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RideChatDetailApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = RideChat.objects.all()
    serializer_class = RideChatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
