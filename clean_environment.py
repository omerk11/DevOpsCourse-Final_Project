import requests

try:
    requests.get('http://0.0.0.0:5000/stop_server', timeout=5)
    print("Backend servers stopped")

except requests.exceptions.ReadTimeout:
    print("The request timeout -  504 error")
