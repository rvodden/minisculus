"""Entrypoint for challenge number 4"""
import json
from requests import put
from pprint import PrettyPrinter

from minisculus import MarkFour

SUBMISSION_URL: str = "http://minisculuschallenge.com/4baecf8ca3f98dc13eeecbac263cd3ed"

pprint = PrettyPrinter().pprint


def main():
    mark_four: MarkFour = MarkFour(7, 2)
    encoded_string: str = mark_four.decode(
        "WZyDsL3u'0TfxP06RtSSF 'DbzhdyFIAu2 zF "
        "f5KE\"SOQTNA8A\"NCKPOKG5D9GSQE'M86IGFMKE6'K4pEVPK!bv83I"
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
