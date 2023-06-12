from model_bakery.recipe import Recipe, foreign_key
from datetime import datetime
from django.utils.timezone import make_aware
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

example_client = Recipe(
    Client,
    first_name="client_name",
    last_name="client_lastname",
    email="example_client@gmail.com",
    associated_card_number="1234567890123456",
    associated_card_type="debit",
    score=4.8,
)

example_driver = Recipe(
    Driver,
    first_name="driver_name",
    last_name="driver_lastname",
    email="example_driver@gmail.com",
    rut=19687866,
    bank="banco estado",
    bank_account_number="19687866",
    car_plate="BBCL34",
    car_brand="suzuki",
    car_model="swift v.1.2 cvt glx plus",
    car_color="black",
    score=4.1,
)

example_trip_id = Recipe(
    Trip,
    id=1,
    client=foreign_key(example_client),
    driver=foreign_key(example_driver),
    cost=4750,
    created_at=make_aware(datetime.now()),
    payment="cash",
    completion_state="completed",
    score=5.0,
)

example_trip_no_id = Recipe(
    Trip,
    client=foreign_key(example_client),
    driver=foreign_key(example_driver),
    cost=4750,
    created_at=make_aware(datetime.now()),
    payment="cash",
    completion_state="completed",
    score=5.0,
)

example_route = Recipe(
    Route,
    lat_coord=-33.457607980702,
    lon_coord=-70.664476251628,
    timestamp=make_aware(
        datetime.strptime("23/2/2020 11:12:22.234513", "%d/%m/%Y %H:%M:%S.%f")
    ),
    trip=foreign_key(example_trip_id),
)

example_background_check = Recipe(
    BackgroundCheck,
    driver=foreign_key(example_driver),
    age=26,
    status_of_procedure="accepted",
)

example_client_payment = Recipe(
    ClientPayment,
    client=foreign_key(example_client),
    created_at=make_aware(
        datetime.strptime("23/2/2020 11:12:22.234513", "%d/%m/%Y %H:%M:%S.%f")
    ),
    trip=foreign_key(example_trip_no_id),
    amount=5225,
    payment_method="cash",
    status="pending",
)

example_driver_payment = Recipe(
    DriverPayment,
    driver=foreign_key(example_driver),
    created_at=make_aware(
        datetime.strptime("23/2/2020 11:12:22.234513", "%d/%m/%Y %H:%M:%S.%f")
    ),
    trip=foreign_key(example_trip_no_id),
    amount=5225,
    bank="banco estado",
    bank_account_number="19687866",
    status="pending",
)

example_ride_chat = Recipe(
    RideChat,
    driver=foreign_key(example_driver),
    client=foreign_key(example_client),
    trip=foreign_key(example_trip_no_id),
    created_at=make_aware(
        datetime.strptime("23/2/2020 11:12:22.234513", "%d/%m/%Y %H:%M:%S.%f")
    ),
)
