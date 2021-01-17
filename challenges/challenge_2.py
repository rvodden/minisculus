"""Entrypoint for challenge number 1"""
import json
from requests import put
from pprint import PrettyPrinter

from minisculus import MarkTwo

SUBMISSION_URL: str = "http://minisculuschallenge.com/2077f244def8a70e5ea758bd8352fcd8"

pprint = PrettyPrinter().pprint


def main():
    mark_one: MarkTwo = MarkTwo(9, 3)
    encoded_string: str = mark_one.encode_string(
        "The Desert Fox will move 30 tanks " "to Calais at dawn"
    )
    payload = {"answer": encoded_string}

    response = put(SUBMISSION_URL, data=json.dumps(payload).encode("UTF-8"))
    if response.status_code == 200:
        response_content = json.loads(response.content)
        pprint(response_content)
    else:
        pprint(response)


if __name__ == "__main__":
    main()
