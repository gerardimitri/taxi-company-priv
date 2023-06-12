import pytest
from rest_framework import status
from django.utils.timezone import make_aware
from datetime import datetime
from model_bakery import baker
from app.serializers import (
    ClientSerializer,
    DriverSerializer,
    RouteSerializer,
    TripSerializer,
    BackgroundCheckSerializer,
    ClientPaymentSerializer,
    DriverPaymentSerializer,
    RideChatSerializer,
)

# --- project ---


class TestTripListApiView:
    @pytest.mark.django_db
    def test_trips_get(self, client):
        trip1 = baker.make_recipe("app.tests.example_trip_id")
        trip2 = baker.make_recipe(
            "app.tests.example_trip_id",
            id=2,
            cost=3500,
            score=4.4,
        )
        trip_list = []
        trip_list.append(TripSerializer(trip1).data)
        trip_list.append(TripSerializer(trip2).data)
        request = client.get("/api/trips/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == trip_list


class TestTripDetailApiView:
    @pytest.mark.django_db
    def test_detail_trip_get(self, client):
        trip = baker.make_recipe("app.tests.example_trip_id")
        id = trip.id
        request = client.get(f"/api/trips/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == TripSerializer(trip).data

    @pytest.mark.django_db
    def test_detail_no_trip_get(self, client):
        request = client.get("/api/trips/1/")
        assert request.status_code == 404


class TestClientListApiView:
    @pytest.mark.django_db
    def test_clients_get(self, client):
        client1 = baker.make_recipe("app.tests.example_client")
        client2 = baker.make_recipe(
            "app.tests.example_client",
            id=2,
        )
        client_list = []
        client_list.append(ClientSerializer(client1).data)
        client_list.append(ClientSerializer(client2).data)
        request = client.get("/api/clients/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == client_list


class TestClientDetailApiView:
    @pytest.mark.django_db
    def test_detail_client_get(self, client):
        uber_client = baker.make_recipe("app.tests.example_client")
        id = uber_client.id
        request = client.get(f"/api/clients/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == ClientSerializer(uber_client).data

    @pytest.mark.django_db
    def test_detail_no_client_get(self, client):
        request = client.get("/api/clients/1/")
        assert request.status_code == 404


class TestDriverListApiView:
    @pytest.mark.django_db
    def test_drivers_get(self, client):
        driver1 = baker.make_recipe("app.tests.example_driver")
        driver2 = baker.make_recipe(
            "app.tests.example_driver",
            id=2,
        )
        driver_list = []
        driver_list.append(DriverSerializer(driver1).data)
        driver_list.append(DriverSerializer(driver2).data)
        request = client.get("/api/drivers/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == driver_list


class TestDriverDetailApiView:
    @pytest.mark.django_db
    def test_detail_driver_get(self, client):
        uber_driver = baker.make_recipe("app.tests.example_driver")
        id = uber_driver.id
        request = client.get(f"/api/drivers/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == DriverSerializer(uber_driver).data

    @pytest.mark.django_db
    def test_detail_no_driver_get(self, client):
        request = client.get("/api/drivers/1/")
        assert request.status_code == 404


class TestRouteListApiView:
    @pytest.mark.django_db
    def test_routes_get(self, client):
        route1 = baker.make_recipe("app.tests.example_route")
        route2 = baker.make_recipe(
            "app.tests.example_route",
            id=2,
        )
        route_list = []
        route_list.append(RouteSerializer(route1).data)
        route_list.append(RouteSerializer(route2).data)
        request = client.get("/api/routes/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        print(response)
        assert response == route_list


class TestRouteDetailApiView:
    @pytest.mark.django_db
    def test_detail_route_get(self, client):
        route = baker.make_recipe("app.tests.example_route")
        id = route.id
        request = client.get(f"/api/routes/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == RouteSerializer(route).data

    @pytest.mark.django_db
    def test_detail_no_route_get(self, client):
        request = client.get("/api/routes/1/")
        assert request.status_code == 404


class TestBackgroundCheckListApiView:
    @pytest.mark.django_db
    def test_background_check_get(self, client):
        background_check1 = baker.make_recipe("app.tests.example_background_check")
        background_check2 = baker.make_recipe(
            "app.tests.example_background_check",
            id=2,
        )
        background_check_list = []
        background_check_list.append(
            BackgroundCheckSerializer(background_check1).data
        )
        background_check_list.append(
            BackgroundCheckSerializer(background_check2).data
        )
        request = client.get("/api/background-checks/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == background_check_list


class TestBackgroundCheckDetailApiView:
    @pytest.mark.django_db
    def test_detail_background_check_get(self, client):
        background_check = baker.make_recipe("app.tests.example_background_check")
        id = background_check.id
        request = client.get(f"/api/background-checks/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == BackgroundCheckSerializer(background_check).data

    @pytest.mark.django_db
    def test_detail_no_background_check_get(self, client):
        request = client.get("/api/background-checks/1/")
        assert request.status_code == 404


class TestClientPaymentListApiView:
    @pytest.mark.django_db
    def test_client_payment_get(self, client):
        client_payment1 = baker.make_recipe("app.tests.example_client_payment")
        client_payment2 = baker.make_recipe(
            "app.tests.example_client_payment",
            id=2,
        )
        client_payment_list = []
        client_payment_list.append(ClientPaymentSerializer(client_payment1).data)
        client_payment_list.append(ClientPaymentSerializer(client_payment2).data)
        request = client.get("/api/client-payments/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == client_payment_list


class TestClientPaymentDetailApiView:
    @pytest.mark.django_db
    def test_detail_client_payment_get(self, client):
        client_payment = baker.make_recipe("app.tests.example_client_payment")
        id = client_payment.id
        request = client.get(f"/api/client-payments/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == ClientPaymentSerializer(client_payment).data

    @pytest.mark.django_db
    def test_detail_no_client_payment_get(self, client):
        request = client.get("/api/client-payments/1/")
        assert request.status_code == 404


class TestDriverPaymentListApiView:
    @pytest.mark.django_db
    def test_driver_payment_get(self, client):
        driver_payment1 = baker.make_recipe("app.tests.example_driver_payment")
        driver_payment2 = baker.make_recipe(
            "app.tests.example_driver_payment",
            id=2,
        )
        driver_payment_list = []
        driver_payment_list.append(DriverPaymentSerializer(driver_payment1).data)
        driver_payment_list.append(DriverPaymentSerializer(driver_payment2).data)
        request = client.get("/api/driver-payments/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == driver_payment_list


class TestDriverPaymentDetailApiView:
    @pytest.mark.django_db
    def test_detail_driver_payment_get(self, client):
        driver_payment = baker.make_recipe("app.tests.example_driver_payment")
        id = driver_payment.id
        request = client.get(f"/api/driver-payments/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == DriverPaymentSerializer(driver_payment).data

    @pytest.mark.django_db
    def test_detail_no_driver_payment_get(self, client):
        request = client.get("/api/driver-payments/1/")
        assert request.status_code == 404


class TestRideChatListApiView:
    @pytest.mark.django_db
    def test_ride_chat_get(self, client):
        ride_chat1 = baker.make_recipe("app.tests.example_ride_chat")
        ride_chat2 = baker.make_recipe(
            "app.tests.example_ride_chat",
            created_at=make_aware(
                datetime.strptime(
                    "23/2/2020 11:15:25.234513", "%d/%m/%Y %H:%M:%S.%f"
                )
            ),
        )
        ride_chat_list = []
        ride_chat_list.append(RideChatSerializer(ride_chat1).data)
        ride_chat_list.append(RideChatSerializer(ride_chat2).data)
        request = client.get("/api/ride-chats/")
        response = request.data

        assert request.status_code == status.HTTP_200_OK
        assert response == ride_chat_list


class TestRideChatDetailApiView:
    @pytest.mark.django_db
    def test_detail_ride_chat_get(self, client):
        ride_chat = baker.make_recipe("app.tests.example_ride_chat")
        id = ride_chat.id
        request = client.get(f"/api/ride-chats/{id}/")
        response = request.data
        assert request.status_code == status.HTTP_200_OK
        assert response == RideChatSerializer(ride_chat).data

    @pytest.mark.django_db
    def test_detail_no_driver_payment_get(self, client):
        request = client.get("/api/ride-chats/1/")
        assert request.status_code == 404
