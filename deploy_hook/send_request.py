import requests


def send_post_request(url, data):
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.text  # Or response.json() if expecting JSON
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


# Example usage:
url = "http://192.168.10.64:5000/webhook"
data = {"name": "Alice", "age": 30}
result = send_post_request(url, data)
print(result)
