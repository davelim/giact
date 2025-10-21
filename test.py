#!/usr/bin/env python

import json
import pprint
import requests

# from .globals import ServiceFlags
from globals import ServiceFlags


BASE_URL = "https://sandbox.api.giact.com"
API_PATH = "/verificationservices/web_api"
INQUIRIES_ENDPOINT = "inquiries_v5_9"
ERROR_LOG_ENDPOINT = "error_log_items"

ERROR_LOG_ITEM = 'See the location in the header for the link to Error Log Item.'


def cat():
    url = "https://cataas.com/cat"
    response = requests.request("GET", url)
    print(response)


def creds():
    with open("./creds.json") as fp:
        data = json.load(fp)
    return data["username"], data["password"]


def giact_request(method, endpoint, data=None):
    url = f"{BASE_URL}{API_PATH}/{endpoint}"
    print(f"> {method} {url} {data}")

    username, password = creds()
    response = requests.request(
        method, url, auth=(username, password), json=data
    )
    return response


def giact_get_status():
    return giact_request("GET", "status")


def giact_get_error_log(id):
    # TODO: start here, handle "?start={start}&end={end}"
    return giact_request("GET", f"error_log_items/{id}")


def giact_post_inquiry(data):
    response = giact_request("POST", INQUIRIES_ENDPOINT, data)
    print(f"POST {INQUIRIES_ENDPOINT} {data}... {response.status_code}")

    if not response.ok:
        if response.json().find(ERROR_LOG_ITEM) != -1:
            error_log_id = response.headers['Location'].split('/')[-1]
            error_log_response = giact_get_error_log(error_log_id)
            print("> ERROR LOG ITEM...")
            pprint.pprint(error_log_response.json())

    return response


def giact_get_inquiry(id, start_date=None, end_date=None):
    if id is not None:
        end_point = f"{INQUIRIES_ENDPOINT}/{id}"
    elif start_date is not None and end_date is not None:
        end_point = f"{INQUIRIES_ENDPOINT}/{start_date}/{end_date}"
    else:
        end_point = None

    if end_point:
        # TODO: get error log?
        return giact_request("GET", end_point)
    else:
        # TODO: probably a better way of doing this.
        response = requests.Response()
        response.ok = False
        response.status_code = 404
        return response


def giact_gVerify(
    unique_id="verify test1",
    data={
        "ServiceFlags": [ServiceFlags.VERIFY],
        "BankAccountEntity": {
            "RoutingNumber": "122105278",
            "AccountNumber": "0000000016",
            "AccountType": 1
        }
    }
):
    data["UniqueId"] = f"{unique_id}"

    post_response = giact_post_inquiry(data)
    if post_response.ok:
        item_reference_id = post_response.json()["ItemReferenceID"]
        # 404: not found
        # get_response = giact_get_inquiry(1)
        # 400: invalid request, null entry for 'id'
        # get_response = giact_get_inquiry("foo")

        giact_get_inquiry(item_reference_id)


def giact_gVerify_gAuthenticate(
    unique_id="verify + authenticate test1",
    data={
        "ServiceFlags": [ServiceFlags.VERIFY, ServiceFlags.AUTHENTICATE],
        "BankAccountEntity": {
            "RoutingNumber": "122105278",
            "AccountNumber": "0000000016",
            "AccountType": 1
        },
        "PersonEntity": {
            # 400: field validation error, see 'location' in header.
            # - error from header['Location']: "If gAuthenticate... is
            #   enabled, FirstName... required."
            # "First_Name": "jane",

            # NOTE:
            # - "foo bar" returns 5 ("RiskAlert") for "VerificationResult"
            # - "jane doe" returns 6 ("Pass") for "VerificationResult"
            # "FirstName": "foo",
            # "LastName": "bar",

            "FirstName": "jane",
            "LastName": "doe",
            "AddressEntity": {
                "AddressLine1": "",
                "City": "",
                "State": "",
                "ZipCode": "",
                "Country": ""
            },
            "PhoneNumber": "",
            "TaxID": "",
            "DateOfBirth": ""
        }
    }
):
    data["UniqueId"] = f"{unique_id}"

    print("POST verify + authenticate...")
    post_response = giact_post_inquiry(data)
    if post_response.ok:
        item_reference_id = post_response.json()["ItemReferenceID"]
        print("GET verify + authenticate...")
        giact_get_inquiry(item_reference_id)


if __name__ == '__main__':
    # cat()
    # giact_status()

    giact_gVerify()
    # - 400: field validation error, see 'location' in header.
    #   - location: "enabled service requires fields from PersonEntity..."
    giact_gVerify(
        "verify test2: field validation error (400)",
        {
            "ServiceFlags": [ServiceFlags.VERIFY, ServiceFlags.AUTHENTICATE],
            "BankAccountEntity": {
                "RoutingNumber": "122105278",
                "AccountNumber": "0000000016",
                "AccountType": 1
            }
        }
    )

    # giact_gVerify_gAuthenticate()
