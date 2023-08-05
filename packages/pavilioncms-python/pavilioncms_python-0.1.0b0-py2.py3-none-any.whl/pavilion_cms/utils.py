import requests

from pavilion_cms.exceptions import (
    UserAuthError,
    UserNotAuthorized,
    BadRequest,
    ResourceNotFound,
)

PAGE_SIZE = 10


def handle_errors(response):
    if response.status_code == requests.codes.unauthorized:
        raise UserAuthError()
    if response.status_code == requests.codes.bad_request:
        raise BadRequest()
    if response.status_code == requests.codes.not_found:
        raise ResourceNotFound()
    if response.status_code == requests.codes.forbidden:
        raise UserNotAuthorized()


def handle_api_list_response(response):
    total_pages = int(response.json()["count"]) // PAGE_SIZE
    results = response.json()["results"]
    count = response.json()["count"]

    json_response = {
        "metadata": {
            "total_pages": total_pages if total_pages > 0 else 1,
            "count": count,
        },
        "results": results,
    }
    return json_response
