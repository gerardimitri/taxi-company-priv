import pytest
from app.models import *
from Privacy.annotations import *
from Privacy.data_taxonomy import *

class TestClient:
    @pytest.fixture
    def client(self):
        return Client()

    def test_client_model_has_privacy_meta(self):
        assert hasattr(Client, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(Client.PrivacyMeta, PrivacyAnnotation)

    def test_client_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(Client)
        model_fields.remove('id')
        assert model_fields == Client.PrivacyMeta.get_fields()

    def test_client_privacy_meta_fields_have_categories(self):
        for field in Client.PrivacyMeta.get_fields():
            d = eval(f'Client.PrivacyMeta.{field}')
            # print(list(map(lambda x: x.fides_key,TAXONOMY.data_category)))
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_client_privacy_meta_fields_have_subjects(self):
        for field in Client.PrivacyMeta.get_fields():
            d = eval(f'Client.PrivacyMeta.{field}')
            # print(list(map(lambda x: x.fides_key,TAXONOMY.data_subject)))
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))


    def test_client_privacy_meta_fields_have_retention_time(self):
        for field in Client.PrivacyMeta.get_fields():
            d = eval(f'Client.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0

        

class TestDriver:
    @pytest.fixture
    def driver(self):
        return Driver()

    def test_driver_model_has_privacy_meta(self):
        assert hasattr(Driver, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(Driver.PrivacyMeta, PrivacyAnnotation)

    def test_driver_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(Driver)
        model_fields.remove('id')
        assert model_fields == Driver.PrivacyMeta.get_fields()

    def test_driver_privacy_meta_fields_have_categories(self):
        for field in Driver.PrivacyMeta.get_fields():
            d = eval(f'Driver.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_driver_privacy_meta_fields_have_subjects(self):
        for field in Driver.PrivacyMeta.get_fields():
            d = eval(f'Driver.PrivacyMeta.{field}')
            #assert d['subject'] in list(map(lambda x: x.fides_key,TAXONOMY.data_subject)) or d['subject'] is None
        
            # print(list(map(lambda x: x.fides_key,TAXONOMY.data_subject)))
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))


    def test_driver_privacy_meta_fields_have_retention_time(self):
        for field in Driver.PrivacyMeta.get_fields():
            d = eval(f'Driver.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0


class TestTrip:
    @pytest.fixture
    def trip(self):
        return Trip()

    def test_trip_model_has_privacy_meta(self):
        assert hasattr(Trip, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(Trip.PrivacyMeta, PrivacyAnnotation)

    def test_trip_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(Trip)
        model_fields.remove('id')
        assert model_fields == Trip.PrivacyMeta.get_fields()

    def test_trip_privacy_meta_fields_have_categories(self):
        for field in Trip.PrivacyMeta.get_fields():
            d = eval(f'Trip.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_trip_privacy_meta_fields_have_subjects(self):
        for field in Trip.PrivacyMeta.get_fields():
            d = eval(f'Trip.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_trip_privacy_meta_fields_have_retention_time(self):
        for field in Trip.PrivacyMeta.get_fields():
            d = eval(f'Trip.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0



class TestRoute:
    @pytest.fixture
    def route(self):
        return Route()

    def test_route_model_has_privacy_meta(self):
        assert hasattr(Route, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(Route.PrivacyMeta, PrivacyAnnotation)

    def test_route_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(Route)
        model_fields.remove('id')
        assert model_fields == Route.PrivacyMeta.get_fields()

    def test_route_privacy_meta_fields_have_categories(self):
        for field in Route.PrivacyMeta.get_fields():
            d = eval(f'Route.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_route_privacy_meta_fields_have_subjects(self):
        for field in Route.PrivacyMeta.get_fields():
            d = eval(f'Route.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_route_privacy_meta_fields_have_retention_time(self):
        for field in Route.PrivacyMeta.get_fields():
            d = eval(f'Route.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0


class TestBackgroundCheck:
    @pytest.fixture
    def backgroundcheck(self):
        return BackgroundCheck()

    def test_backgroundcheck_model_has_privacy_meta(self):
        assert hasattr(BackgroundCheck, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(BackgroundCheck.PrivacyMeta, PrivacyAnnotation)

    def test_backgroundcheck_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(BackgroundCheck)
        model_fields.remove('id')
        assert model_fields == BackgroundCheck.PrivacyMeta.get_fields()

    def test_backgroundcheck_privacy_meta_fields_have_categories(self):
        for field in BackgroundCheck.PrivacyMeta.get_fields():
            d = eval(f'BackgroundCheck.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_backgroundcheck_privacy_meta_fields_have_subjects(self):
        for field in BackgroundCheck.PrivacyMeta.get_fields():
            d = eval(f'BackgroundCheck.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_backgroundcheck_privacy_meta_fields_have_retention_time(self):
        for field in BackgroundCheck.PrivacyMeta.get_fields():
            d = eval(f'BackgroundCheck.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0

class TestClientPayment:
    @pytest.fixture
    def clientpayment(self):
        return ClientPayment()

    def test_clientpayment_model_has_privacy_meta(self):
        assert hasattr(ClientPayment, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(ClientPayment.PrivacyMeta, PrivacyAnnotation)

    def test_clientpayment_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(ClientPayment)
        model_fields.remove('id')
        assert model_fields == ClientPayment.PrivacyMeta.get_fields()

    def test_clientpayment_privacy_meta_fields_have_categories(self):
        for field in ClientPayment.PrivacyMeta.get_fields():
            d = eval(f'ClientPayment.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_clientpayment_privacy_meta_fields_have_subjects(self):
        for field in ClientPayment.PrivacyMeta.get_fields():
            d = eval(f'ClientPayment.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_clientpayment_privacy_meta_fields_have_retention_time(self):
        for field in ClientPayment.PrivacyMeta.get_fields():
            d = eval(f'ClientPayment.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0

class TestDriverPayment:
    @pytest.fixture
    def driverpayment(self):
        return DriverPayment()

    def test_driverpayment_model_has_privacy_meta(self):
        assert hasattr(DriverPayment, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(DriverPayment.PrivacyMeta, PrivacyAnnotation)

    def test_driverpayment_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(DriverPayment)
        model_fields.remove('id')
        assert model_fields == DriverPayment.PrivacyMeta.get_fields()

    def test_driverpayment_privacy_meta_fields_have_categories(self):
        for field in DriverPayment.PrivacyMeta.get_fields():
            d = eval(f'DriverPayment.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))

    def test_driverpayment_privacy_meta_fields_have_subjects(self):
        for field in DriverPayment.PrivacyMeta.get_fields():
            d = eval(f'DriverPayment.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_driverpayment_privacy_meta_fields_have_retention_time(self):
        for field in DriverPayment.PrivacyMeta.get_fields():
            d = eval(f'DriverPayment.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0


class TestRideChat:
    @pytest.fixture
    def ridechat(self):
        return RideChat()
    
    def test_ridechat_model_has_privacy_meta(self):
        assert hasattr(RideChat, "PrivacyMeta")

    def test_privacymeta_inherits_from_privacyannotation(self):
        assert issubclass(RideChat.PrivacyMeta, PrivacyAnnotation)

    def test_ridechat_model_has_privacy_meta_fields(self):
        model_fields = get_model_fields(RideChat)
        model_fields.remove('id')
        assert model_fields == RideChat.PrivacyMeta.get_fields()

    def test_ridechat_privacy_meta_fields_have_categories(self):
        for field in RideChat.PrivacyMeta.get_fields():
            d = eval(f'RideChat.PrivacyMeta.{field}')
            assert d['category'] in list(map(lambda x: x.fides_key,TAXONOMY.data_category))
    
    def test_ridechat_privacy_meta_fields_have_subjects(self):
        for field in RideChat.PrivacyMeta.get_fields():
            d = eval(f'RideChat.PrivacyMeta.{field}')
            if d['subject'] is None:
                assert True
            else:
                subjects = d['subject'].split(',')
                for subject in subjects:
                    assert subject in list(map(lambda x: x.fides_key,TAXONOMY.data_subject))

    def test_ridechat_privacy_meta_fields_have_retention_time(self):
        for field in RideChat.PrivacyMeta.get_fields():
            d = eval(f'RideChat.PrivacyMeta.{field}')
            assert "retention-time" in d
            assert 'years' in d['retention-time']
            assert 'months' in d['retention-time']
            assert 'days' in d['retention-time']
            assert d['retention-time']['years'] >= 0
            assert d['retention-time']['months'] >= 0
            assert d['retention-time']['days'] >= 0