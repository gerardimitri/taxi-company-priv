import io
from datetime import datetime
from django.utils.timezone import make_aware
from model_bakery import baker
import pytest
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from app.models import (
    Client,
    Driver,
    Route,
    Trip,
    BackgroundCheck,
    ClientPayment,
    DriverPayment,
    RideChat,
)
from app.serializers import (
    ClientSerializer,
    DriverSerializer,
    RouteNoTripSerializer,
    RouteSerializer,
    TripSerializer,
    BackgroundCheckSerializer,
    ClientPaymentSerializer,
    DriverPaymentSerializer,
    RideChatSerializer,
)

# --- project ---

# fixtures to be seen for all test classes


@pytest.fixture
def client_and_serializer():
    client = baker.make_recipe("app.tests.example_client")

    expected_client_serializer = {
        "first_name": client.first_name,
        "last_name": client.last_name,
        "email": client.email,
        "associated_card_number": client.associated_card_number,
        "associated_card_type": client.associated_card_type,
        "score": client.score,
    }

    return [client, expected_client_serializer]


@pytest.fixture
def driver_and_serializer():
    driver = baker.make_recipe("app.tests.example_driver")

    expected_driver_serializer = {
        "first_name": driver.first_name,
        "last_name": driver.last_name,
        "email": driver.email,
        "rut": driver.rut,
        "bank": driver.bank,
        "bank_account_number": driver.bank_account_number,
        "car_plate": driver.car_plate,
        "car_brand": driver.car_brand,
        "car_model": driver.car_model,
        "car_color": driver.car_color,
        "score": driver.score,
    }

    return [driver, expected_driver_serializer]


@pytest.fixture
def trip_and_serializer_id():
    trip = baker.make_recipe("app.tests.example_trip_id")

    expected_trip_serializer = {
        "client": trip.client_id,
        "driver": trip.driver_id,
        "cost": trip.cost,
        "created_at": trip.created_at.isoformat(),
        "payment": trip.payment,
        "completion_state": trip.completion_state,
        "score": trip.score,
        "trip_routes": [],
    }

    return [trip, expected_trip_serializer]


@pytest.fixture
def trip_and_serializer_no_id():
    trip = baker.make_recipe("app.tests.example_trip_no_id")

    expected_trip_serializer = {
        "client": trip.client_id,
        "driver": trip.driver_id,
        "cost": trip.cost,
        "created_at": trip.created_at.isoformat(),
        "payment": trip.payment,
        "completion_state": trip.completion_state,
        "score": trip.score,
        "trip_routes": [],
    }

    return [trip, expected_trip_serializer]


@pytest.fixture
def route_and_serializer():
    route = baker.make_recipe("app.tests.example_route")

    expected_route_serializer = {
        "lat_coord": route.lat_coord,
        "lon_coord": route.lon_coord,
        "timestamp": route.timestamp.isoformat(),
        "trip": route.trip_id,
    }

    expected_route_no_trip_serializer = {
        "lat_coord": route.lat_coord,
        "lon_coord": route.lon_coord,
        "timestamp": route.timestamp.isoformat(),
    }

    return [route, expected_route_serializer, expected_route_no_trip_serializer]


@pytest.fixture
def background_check_and_serializer():
    background_check = baker.make_recipe(
        "app.tests.example_background_check",
        _fill_optional=True,
        _create_files=True,
    )

    expected_background_check_serializer = {
        "driver": background_check.driver_id,
        "age": background_check.age,
        "criminal_record": background_check.criminal_record.url,
        "profile_headshot": background_check.profile_headshot.url,
        "id_photo": background_check.id_photo.url,
        "status_of_procedure": background_check.status_of_procedure,
    }

    return [background_check, expected_background_check_serializer]


@pytest.fixture
def client_payment_and_serializer():
    client_payment = baker.make_recipe("app.tests.example_client_payment")

    expected_client_payment_serializer = {
        "client": client_payment.client_id,
        "created_at": client_payment.created_at.isoformat(),
        "trip": client_payment.trip_id,
        "amount": client_payment.amount,
        "payment_method": client_payment.payment_method,
        "status": client_payment.status,
    }

    return [client_payment, expected_client_payment_serializer]


@pytest.fixture
def driver_payment_and_serializer():
    driver_payment = baker.make_recipe("app.tests.example_driver_payment")

    expected_driver_payment_serializer = {
        "driver": driver_payment.driver_id,
        "created_at": driver_payment.created_at.isoformat(),
        "trip": driver_payment.trip_id,
        "amount": driver_payment.amount,
        "bank": driver_payment.bank,
        "bank_account_number": driver_payment.bank_account_number,
        "status": driver_payment.status,
    }

    return [driver_payment, expected_driver_payment_serializer]


@pytest.fixture
def ride_chat_and_serializer():
    ride_chat = baker.make_recipe("app.tests.example_ride_chat")

    expected_ride_chat_serializer = {
        "driver": ride_chat.driver_id,
        "client": ride_chat.client_id,
        "created_at": ride_chat.created_at.isoformat(),
        "trip": ride_chat.trip_id,
        "chat": ride_chat.chat,
    }

    return [ride_chat, expected_ride_chat_serializer]


# test classes


class TestClientSerializer:
    @pytest.mark.django_db
    def test_client_serialization(self, client_and_serializer):
        client = client_and_serializer[0]
        expected_serializer_data = client_and_serializer[1]
        serializer_data = ClientSerializer(client).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_client_deserialization(self, client_and_serializer):
        client = client_and_serializer[0]
        content = JSONRenderer().render(client_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = ClientSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        clients = Client.objects.all()

        assert clients.count() == 2
        assert clients.last().first_name == client.first_name
        assert clients.last().last_name == client.last_name


class TestDriverSerializer:
    @pytest.mark.django_db
    def test_driver_serialization(self, driver_and_serializer):
        driver = driver_and_serializer[0]
        expected_serializer_data = driver_and_serializer[1]
        serializer_data = DriverSerializer(driver).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_driver_deserialization(self, driver_and_serializer):
        driver = driver_and_serializer[0]
        content = JSONRenderer().render(driver_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = DriverSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        drivers = Driver.objects.all()

        assert drivers.count() == 2
        assert drivers.last().first_name == driver.first_name
        assert drivers.last().last_name == driver.last_name


class TestRouteSerializer:
    @pytest.mark.django_db
    def test_route_serialization(self, route_and_serializer):
        route = route_and_serializer[0]

        expected_no_trip_serializer_data = route_and_serializer[2]
        no_trip_serializer_data = RouteNoTripSerializer(route).data
        expected_serializer_data = route_and_serializer[1]
        serializer_data = RouteSerializer(route).data

        assert serializer_data == expected_serializer_data
        assert no_trip_serializer_data == expected_no_trip_serializer_data

    @pytest.mark.django_db
    def test_route_deserialization(
        self,
        route_and_serializer,
    ):
        route = route_and_serializer[0]
        expected_serializer = route_and_serializer[1]
        content = JSONRenderer().render(expected_serializer)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = RouteSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        routes = Route.objects.all()

        assert routes.count() == 2
        assert routes.last().lat_coord == route.lat_coord
        assert routes.last().lon_coord == route.lon_coord
        assert routes.last().trip_id == 1


class TestTripSerializer:
    @pytest.mark.django_db
    def test_trip_serialization(
        self,
        trip_and_serializer_id,
    ):

        route1 = baker.make_recipe("app.tests.example_route")
        example_timestamp = make_aware(
            datetime.strptime("23/2/2020 11:08:22.234513", "%d/%m/%Y %H:%M:%S.%f")
        )
        route2 = baker.make_recipe(
            "app.tests.example_route", timestamp=example_timestamp
        )

        trip = trip_and_serializer_id[0]
        expected_serializer_data = trip_and_serializer_id[1]
        expected_serializer_data["trip_routes"].append(
            RouteNoTripSerializer(route2).data
        )
        expected_serializer_data["trip_routes"].append(
            RouteNoTripSerializer(route1).data
        )
        serializer_data = TripSerializer(trip).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_trip_deserialization(self, trip_and_serializer_no_id):
        trip = trip_and_serializer_no_id[0]
        expected_serializer = trip_and_serializer_no_id[1]
        content = JSONRenderer().render(expected_serializer)
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = TripSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        trips = Trip.objects.all()

        assert Trip.objects.all().count() == 2
        assert trips.last().created_at == trip.created_at
        assert trips.last().cost == trip.cost


class TestBackgroundCheckSerializer:
    @pytest.mark.django_db
    def test_background_check_serialization(self, background_check_and_serializer):
        background_check = background_check_and_serializer[0]
        expected_serializer_data = background_check_and_serializer[1]
        serializer_data = BackgroundCheckSerializer(background_check).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_background_check_deserialization(
        self, background_check_and_serializer
    ):
        background_check = background_check_and_serializer[0]
        content = JSONRenderer().render(background_check_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        data["criminal_record"] = background_check.criminal_record
        data["profile_headshot"] = background_check.profile_headshot
        data["id_photo"] = background_check.id_photo
        serializer = BackgroundCheckSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        background_checks = BackgroundCheck.objects.all()

        assert background_checks.count() == 2
        assert background_checks.last().driver_id == background_check.driver_id
        assert background_checks.last().id_photo == background_check.id_photo


class TestClientPaymentSerializer:
    @pytest.mark.django_db
    def test_client_payment_serialization(self, client_payment_and_serializer):
        client_payment = client_payment_and_serializer[0]
        expected_serializer_data = client_payment_and_serializer[1]
        serializer_data = ClientPaymentSerializer(client_payment).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_client_payment_deserialization(self, client_payment_and_serializer):
        client_payment = client_payment_and_serializer[0]
        content = JSONRenderer().render(client_payment_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = ClientPaymentSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        client_payments = ClientPayment.objects.all()

        assert client_payments.count() == 2
        assert client_payments.last().client_id == client_payment.client_id
        assert client_payments.last().trip_id == client_payment.trip_id
        assert client_payments.last().amount == client_payment.amount
        assert client_payments.last().created_at == client_payment.created_at


class TestDriverPaymentSerializer:
    @pytest.mark.django_db
    def test_driver_payment_serialization(self, driver_payment_and_serializer):
        driver_payment = driver_payment_and_serializer[0]
        expected_serializer_data = driver_payment_and_serializer[1]
        serializer_data = DriverPaymentSerializer(driver_payment).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_driver_payment_deserialization(self, driver_payment_and_serializer):
        driver_payment = driver_payment_and_serializer[0]
        content = JSONRenderer().render(driver_payment_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = DriverPaymentSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        driver_payments = DriverPayment.objects.all()

        assert driver_payments.count() == 2
        assert driver_payments.last().driver_id == driver_payment.driver_id
        assert driver_payments.last().trip_id == driver_payment.trip_id
        assert driver_payments.last().amount == driver_payment.amount
        assert driver_payments.last().created_at == driver_payment.created_at


class TestRideChatSerializer:
    @pytest.mark.django_db
    def test_ride_Chat_serialization(self, ride_chat_and_serializer):
        ride_chat = ride_chat_and_serializer[0]
        expected_serializer_data = ride_chat_and_serializer[1]
        serializer_data = RideChatSerializer(ride_chat).data

        assert serializer_data == expected_serializer_data

    @pytest.mark.django_db
    def test_ride_chat_deserialization(self, ride_chat_and_serializer):
        ride_chat = ride_chat_and_serializer[0]
        content = JSONRenderer().render(ride_chat_and_serializer[1])
        stream = io.BytesIO(content)
        data = JSONParser().parse(stream)
        serializer = RideChatSerializer(data=data)

        assert serializer.is_valid()
        assert serializer.errors == {}

        serializer.save()
        ride_chats = RideChat.objects.all()

        assert ride_chats.count() == 2
        assert ride_chats.last().driver_id == ride_chat.driver_id
        assert ride_chats.last().client_id == ride_chat.client_id
        assert ride_chats.last().trip_id == ride_chat.trip_id
        assert ride_chats.last().created_at == ride_chat.created_at
        assert ride_chats.last().chat == ride_chat.chat
