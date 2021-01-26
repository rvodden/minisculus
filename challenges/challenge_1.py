"""Entrypoint for challenge number 1"""
import json
from requests import put
from pprint import PrettyPrinter

from minisculus import MarkOne

SUBMISSION_URL: str = "http://minisculuschallenge.com/14f7ca5f6ff1a5afb9032aa5e533ad95"

pprint = PrettyPrinter().pprint


def main():
    mark_one: MarkOne = MarkOne(6)
    encoded_string: str = mark_one.encode("Strong NE Winds!")
    payload = {"answer": encoded_string}

    response = put(SUBMISSION_URL, data=json.dumps(payload).encode("UTF-8"))
    if response.status_code == 200:
        response_content = json.loads(response.content)
        pprint(response_content)
    else:
        pprint(response)


if __name__ == "__main__":
    main()
