import requests

def validate_country(view_func):
    def wrapper(request, *args, **kwargs):
        # Logic to validate country
        user_ip = request.META.get('REMOTE_ADDR')
        if user_ip:
            response = requests.get(f"https://ipapi.co/{user_ip}/json/")
            country = response.json().get('country_name')
            request.country = country

        # Custom logic for the endpoint
        if view_func.__name__ == 'post':  # Adjust with your specific endpoint name
            # Add specific logic here for the endpoint
            pass

        return view_func(request, *args, **kwargs)

    return wrapper


