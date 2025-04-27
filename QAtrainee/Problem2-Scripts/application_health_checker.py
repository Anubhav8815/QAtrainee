
import requests

def check_application(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"The application at {url} is UP.")
        else:
            print(f"The application at {url} is DOWN. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application at {url} is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    check_application(url)
