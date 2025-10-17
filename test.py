import json
import requests


BASE_URL = "https://sandbox.api.giact.com"
API_PATH = "/verificationservices/web_api"

def cat():
    url = "https://cataas.com/cat"
    response = requests.request("GET", url)
    print(response)


def creds():
    with open("creds.json") as fp:
        data = json.load(fp)
    return data["username"], data["password"]


def giact_request(method, endpoint, data=None):
    username, password = creds()
    url = f"{BASE_URL}{API_PATH}/{endpoint}"
    response = requests.request(method, url, auth=(username, password), json=data)
    # print(response.status_code)
    print(response.headers)
    print(response.json())
    if not response.ok:
        # TODO: place holder for now... 'Location' returns error details. What to do?
        response = requests.get(response.headers['Location'], auth=(username, password))
    return response


def giact_inquiries():
    endpoint = "/inquiries_v5_9"
    data = {
        "UniqueId": "test1",
        "ServiceFlags" : ["verify"],
        "BankAccountEntity": {
            "RoutingNumber": "122105278",
            "AccountNumber": "0000000016",
            "AccountType": 1
        }
    }
    print(giact_request("POST", endpoint, data))


def giact_status():
    endpoint = "/status"
    print(giact_request("GET", endpoint))


if __name__ == '__main__':
    # cat()
    giact_inquiries()
    giact_status()
