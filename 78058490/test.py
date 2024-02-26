import requests


def test_api():
    url = "http://nginx:80/"

    response = requests.get(url)
    assert response.status_code == 200, "API did not return 200 OK!"
    assert response.text == "Hello, World!", "API response did not match!"


if __name__ == "__main__":
    test_api()
    print("Test passed!")
