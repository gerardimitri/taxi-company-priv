from django.urls import path

from .views import (
    ClientListApiView,
    ClientDetailApiView,
    DriverListApiView,
    DriverDetailApiView,
    TripListApiView,
    TripDetailApiView,
    RouteListApiView,
    RouteDetailApiView,
    BackgroundCheckListApiView,
    BackgroundCheckDetailApiView,
    ClientPaymentListApiView,
    ClientPaymentDetailApiView,
    DriverPaymentListApiView,
    DriverPaymentDetailApiView,
    RideChatListApiView,
    RideChatDetailApiView,
)

urlpatterns = [
    # --- examples ---
    # path("", views.index, name="index"),
    # --- project ---
    path("clients/", ClientListApiView.as_view()),
    path("clients/<int:pk>/", ClientDetailApiView.as_view()),
    path("drivers/", DriverListApiView.as_view()),
    path("drivers/<int:pk>/", DriverDetailApiView.as_view()),
    path("trips/", TripListApiView.as_view()),
    path("trips/<int:pk>/", TripDetailApiView.as_view()),
    path("routes/", RouteListApiView.as_view()),
    path("routes/<int:pk>/", RouteDetailApiView.as_view()),
    path("background-checks/", BackgroundCheckListApiView.as_view()),
    path("background-checks/<int:pk>/", BackgroundCheckDetailApiView.as_view()),
    path("client-payments/", ClientPaymentListApiView.as_view()),
    path("client-payments/<int:pk>/", ClientPaymentDetailApiView.as_view()),
    path("driver-payments/", DriverPaymentListApiView.as_view()),
    path("driver-payments/<int:pk>/", DriverPaymentDetailApiView.as_view()),
    path("ride-chats/", RideChatListApiView.as_view()),
    path("ride-chats/<int:pk>/", RideChatDetailApiView.as_view()),
]
