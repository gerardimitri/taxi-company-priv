# import pytest
# from django.test import Client
# from rest_framework import status

# Create your tests here.

# --- examples ---

# class TestTaxiExample:
#     @pytest.fixture
#     def client(self):
#         return Client()

#     def test_index_get(self, client):
#         request = client.get("/app/")
#         response = request.data
#         assert isinstance(response["random integer value"], int)

#     def test_index_post_div_success(self, client):
#         data = {"value": 1}
#         request = client.post("/app/", data)
#         assert request.status_code == status.HTTP_200_OK

#     def test_index_post_div_failure(self, client):
#         data = {"value": 0}
#         request = client.post("/app/", data)
#         assert request.status_code == status.HTTP_400_BAD_REQUEST
