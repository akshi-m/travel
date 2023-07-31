from http import client
from django.test import TestCase, Client
from django.urls import reverse
import os

BASE_URL = 'http://127.0.0.1:8000'

script_dir = os.path.dirname(__file__)
rel_path = "../static/images/about1.png"
abs_file_path = os.path.join(script_dir, rel_path)


class TestViews(TestCase):
    def test_AboutView_GET(self):
        client = Client()

        response = client.get(BASE_URL + '/AboutView')
        print("test_AboutView_GET", response)
        self.assertEquals(response.status_code, 302)

    def test_FeedbackView_GET(self):
        client = Client()

        response = client.get(BASE_URL + '/feedback')
        print("test_FeedbackView_GET", response)
        self.assertEquals(response.status_code, 302)

    def test_FeedbackView_POST_success(self):
        client = Client()
        payload = {
            "name": "asd",
            "email": "pu@asd.com",
            "review": "pulsda",
            "image": abs_file_path
        }
        response = client.post(
            BASE_URL + '/feedback',
            data=payload)
        print("test_FeedbackView_POST", response)
        self.assertEquals(response.status_code, 302)

    def test_FeedbackView_POST_fail_image(self):
        client = Client()
        payload = {
            "name": "asd",
            "email": "pu@asd.com",
            "review": "pulsda",
            "image": ''
        }
        response = client.post(
            BASE_URL + '/login',
            data=payload)
        print("test_FeedbackView_POST_fail_image", response)
        self.assertEquals(response.status_code, 301)

    def test_FeedbackView_POST_fail_review(self):
        client = Client()
        payload = {
            "name": "asd",
            "email": "pu@asd.com",
            "review": "",
            "image": abs_file_path
        }
        response = client.post(
            BASE_URL + '/login',
            data=payload)
        print("test_FeedbackView_POST_fail_review", response)
        self.assertEquals(response.status_code, 301)

    def test_SinglePage_GET_success(self):
        client = Client()

        response = client.get(BASE_URL + '/SinglePage/cat=<str:cat>')
        print("test_SinglePage_POST", response)
        self.assertEquals(response.status_code, 302)

    def test_TraveldeskView_GET_success(self):
        client = Client()

        response = client.get(BASE_URL + '/traveldesk')
        print("test_Traveldesk_GET", response)
        self.assertEquals(response.status_code, 302)

    def test_TraveldeskView_POST_success(self):
        client = Client()
        payload = {
            "name": "asd",
            "email": "pu@asd.com",
            "expected_date": "13/09/2022",
            "phone": "9414623588",
            "message": "pulsda",
            "number_of_person": "12"

        }
        response = client.post(
            BASE_URL + '/traveldesk',
            data=payload)
        print("test_TraveldeskView_POST", response)
        self.assertEquals(response.status_code, 302)

    def test_TraveldeskView_POST_fail(self):
        client = Client()
        payload = {
            "name": "asd11",
            "email": "pu@asd.com",
            "expected_date": "13/09/2022",
            "phone": "9414623588",
            "message": "pulsda",
            "number_of_person": "12"

        }
        response = client.post(
            BASE_URL + '/traveldesk',
            data=payload)
        print("test_TraveldeskView_POST", response)
        self.assertEquals(response.status_code, 302)

    def test_SignIn_GET_success(self):
        client = Client()

        response = client.get(BASE_URL + '/login')
        print("test_SignIn_GET", response)
        self.assertEquals(response.status_code, 301)

    def test_SigIn_POST_success(self):
        client = Client()
        payload = {
            'username': 'shubham',
            'password': 'Zxcvbn@1'

        }
        response = client.post(
            BASE_URL + '/login',
            data=payload)
        print("test_SignIn_POST", response)
        self.assertEquals(response.status_code, 301)

    def test_SignOut_GET_success(self):
        client = Client()

        response = client.get(BASE_URL + '/login')
        print("test_SignOut_GET", response)
        self.assertEquals(response.status_code, 301)

    def test_SignUp_GET_success(self):
        client = Client()

        response = client.get(BASE_URL + '/signup')
        print("test_SignUp_GET", response)
        self.assertEquals(response.status_code, 301)

    def test_SignUp_POST_success(self):
        client = Client()

        payload = {
            'username': 'shubham',
            'email': 'shubhamvijayvargiya5@gmail.com',
            'password': 'Zxcvbn@1',
            'password2': 'Zxcvbn@1'

        }
        response = client.post(
            BASE_URL + '/login',
            data=payload)
        print("test_SignIn_POST", response)
        self.assertEquals(response.status_code, 301)

    def test_SignUp_POST_fail(self):
        client = Client()

        payload = {
            'username': 'shubham',
            'email': 'shubhamvijayvargiya5@gmail.com',
            'password': 'Zxcvbn@1',
            'password2': 'Zxcvbn@11'

        }
        response = client.post(
            BASE_URL + '/Signup',
            data=payload)
        print("test_SignIn_POST", response)
        self.assertEquals(response.status_code, 404)
