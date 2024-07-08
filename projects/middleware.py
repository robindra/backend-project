from django.utils.deprecation import MiddlewareMixin
import requests

class CountryValidationMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        user_ip = requests.META.get('REMOTE_ADDR')
        if user_ip:
            response = requests.get(f"https://ipapi.co/{user_ip}/json/")
            country = response.json().get('country_name')
            request.country = country