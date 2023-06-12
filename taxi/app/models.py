from django.db import models
from Privacy.annotations import PrivacyAnnotation

# Create your models here.

# --- examples ---


# class IntegerBox(models.Model):
#     integer = models.IntegerField()

#     def integer_value(self):
#         return self.integer


# --- project ---


class Client(models.Model):
    class PrivacyMeta(PrivacyAnnotation):
        first_name = {'category':'user.name', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        last_name = {'category':'user.name', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        email = {'category':'user.contact.email', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        associated_card_number = {'category':'user.financial.account_number', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        associated_card_type = {'category':'user.financial.account_number', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        score = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        #fields = ["first_name", "last_name", "email", "associated_card_number", "associated_card_type", "score"]

    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField(max_length=254)
    associated_card_number = models.CharField(max_length=16, null=True)
    # debit or credit card
    associated_card_type = models.CharField(max_length=400, null=True)
    score = models.FloatField()

    def __str__(self) -> str:
        full_name = self.first_name + " " + self.last_name
        return full_name

    
        


class Driver(models.Model):
    class PrivacyMeta(PrivacyAnnotation):
        first_name = {'category':'user.name', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        last_name = {'category':'user.name', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        email = {'category':'user.contact.email', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        rut = {'category':'user.government_id.national_identification_number', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        bank = {'category':'user.financial.account_number', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        bank_account_number = {'category':'user.financial.account_number', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        car_plate = {'category':'user.car_details', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        car_brand = {'category':'user.car_details', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        car_model = {'category':'user.car_details', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        car_color = {'category':'user.car_details', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        score = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        #fields = ["first_name", "last_name", "email", "rut", "bank", "bank_account_number", "car_plate", "car_brand", "car_model", "car_color", "score"]

    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    email = models.EmailField(max_length=254)
    rut = models.IntegerField()
    bank = models.CharField(max_length=400)
    bank_account_number = models.CharField(max_length=16)
    car_plate = models.CharField(max_length=6)
    car_brand = models.CharField(max_length=400)
    car_model = models.CharField(max_length=400)
    car_color = models.CharField(max_length=400)
    score = models.FloatField()

    def __str__(self) -> str:
        full_name = self.first_name + " " + self.last_name
        return full_name
    
    


class Trip(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        client = {'category':'user.unique_id', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        driver = {'category':'user.unique_id', 'subject':'employee', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        cost = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        created_at = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        payment = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        completion_state = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        score = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 1, 'months': 0, 'days': 0}}

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,null=True)
    # cost of entire trip in chilean pesos
    cost = models.IntegerField()
    created_at = models.DateTimeField()
    # payment options
    payment = models.CharField(max_length=400)
    # trip completion state
    completion_state = models.CharField(max_length=400)
    score = models.FloatField(null=True)

    def __str__(self) -> str:
        tr = f"Id: {self.pk}, Created at: {self.created_at}, Client: {self.client}, Driver: {self.driver}"
        return tr
    


class Route(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        lat_coord = {'category':'user.location', 'subject':'passenger,employee', 'retention-time':{'years': 0, 'months': 0, 'days': 15}}  # Tambien pertenece a employee
        lon_coord = {'category':'user.location', 'subject':'passenger,employee', 'retention-time':{'years': 0, 'months': 0, 'days': 15}} # Tambien pertenece a employee
        timestamp = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 0, 'months': 0, 'days': 15}}
        trip = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 0, 'months': 0, 'days': 15}}

    lat_coord = models.FloatField()
    lon_coord = models.FloatField()
    timestamp = models.DateTimeField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self) -> str:
        route_resume = f"Trip Id: {self.trip_id}, Timestamp: {self.timestamp}"
        return route_resume
    


# Background data of drivers that apply to taxi company.
class BackgroundCheck(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        driver = {'category':'user.unique_id', 'subject':'employee', 'retention-time':{'years': 100, 'months': 0, 'days': 0}}
        age = {'category':'user.non_specific_age', 'subject':'employee', 'retention-time':{'years': 100, 'months': 0, 'days': 0}}
        criminal_record = {'category':'user.background', 'subject':'employee', 'retention-time':{'years': 100, 'months': 0, 'days': 0}}
        profile_headshot = {'category':'user.profile_photo', 'subject':'employee', 'retention-time':{'years': 100, 'months': 0, 'days': 0}}
        id_photo = {'category':'user.background', 'subject':'employee', 'retention-time':{'years': 100, 'months': 0, 'days': 0}}
        status_of_procedure = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 100, 'months': 0, 'days': 0}}

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    age = models.IntegerField()
    criminal_record = models.FileField(upload_to="criminal_record/")
    profile_headshot = models.FileField(upload_to="profile_headshot/")
    id_photo = models.FileField(upload_to="id_photos/")
    """ status of background check procedure:
        processing, accepted, rejected"""
    status_of_procedure = models.CharField(max_length=400)

    def __str__(self) -> str:
        return f"Driver Id: {self.driver_id}"


# Payments of trips taken by clients
class ClientPayment(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        client = {'category':'user.unique_id', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        created_at = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        trip = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 1, 'months': 0, 'days': 0}}
        amount = {'category':'user.payment', 'subject':'passenger', 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        payment_method = {'category':'user.payment', 'subject':'passenger', 'retention-time':{'years': 2, 'months': 0, 'days': 0}}
        status = {'category':'user.payment', 'subject':'passenger', 'retention-time':{'years': 1, 'months': 0, 'days': 0}}

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    payment_method = models.CharField(max_length=400, null=True)
    """ status of transaction:
        pending, accepted, declined"""
    status = models.CharField(max_length=400)

    def __str__(self) -> str:
        payment_resume = f"Client Id: {self.client_id}, Trip Id: {self.trip_id}"
        return payment_resume

# Payments of trips done by drivers
class DriverPayment(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        driver = {'category':'user.unique_id', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        created_at = {'category':'user.payment', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        trip = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        amount = {'category':'user.payment', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        bank = {'category':'user.payment', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        bank_account_number = {'category':'user.payment', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}
        status = {'category':'user.payment', 'subject':'employee', 'retention-time':{'years': 10, 'months': 0, 'days': 0}}

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True)
    bank = models.CharField(max_length=400, null=True)
    bank_account_number = models.CharField(max_length=16, null=True)
    """ status of transaction:
        pending, accepted, declined"""
    status = models.CharField(max_length=400)

    def __str__(self) -> str:
        payment_resume = f"Driver Id: {self.driver_id}, Trip Id: {self.trip_id}"
        return payment_resume


class RideChat(models.Model):

    class PrivacyMeta(PrivacyAnnotation):
        driver = {'category':'user.unique_id', 'subject':'employee', 'retention-time':{'years': 0, 'months': 3, 'days': 0}}
        client = {'category':'user.unique_id', 'subject':'passenger', 'retention-time':{'years': 0, 'months': 3, 'days': 0}}
        created_at = {'category':'user.social', 'subject':'passenger,employee', 'retention-time':{'years': 0, 'months': 3, 'days': 0}}  # Tambien pertenece a employee
        trip = {'category':'system.operations', 'subject':None, 'retention-time':{'years': 0, 'months': 3, 'days': 0}}
        chat = {'category':'user.social', 'subject':'passenger,employee', 'retention-time':{'years': 0, 'months': 3, 'days': 0}}  # Tambien pertenece a employee

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    chat = models.JSONField()