"""Entrypoint for challenge number 3"""
import json
from requests import put
from pprint import PrettyPrinter

from minisculus import MarkFour

SUBMISSION_URL: str = "http://minisculuschallenge.com/36d80eb0c50b49a509b49f2424e8c805"

pprint = PrettyPrinter().pprint


def main():
    mark_four: MarkFour = MarkFour(4, 7)
    encoded_string: str = mark_four.encode(
        "The white cliffs of Alghero are visible at night"
    )
    pprint(encoded_string)
    payload = {"answer": encoded_string}

    response = put(SUBMISSION_URL, data=json.dumps(payload).encode("UTF-8"))
    if response.status_code == 200:
        response_content = json.loads(response.content)
        pprint(response_content)
    else:
        pprint(response)


if __name__ == "__main__":
    main()
