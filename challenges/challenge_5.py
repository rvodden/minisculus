"""Entrypoint for challenge number 4"""
from pprint import PrettyPrinter

from minisculus._bruteforce import BruteForce

SUBMISSION_URL: str = "http://minisculuschallenge.com/4baecf8ca3f98dc13eeecbac263cd3ed"

pprint = PrettyPrinter().pprint


def main():
    encoded_string: str = (
        "QT4e8MJYVhkls.27BL9,.MSqYSi'IUpAJKWg9Ul9p4o8oUoGy'ITd4d"
        '0AJVsLQp4kKJB2rz4dxfahwUa"Wa.MS!k4hs2yY3k8ymnla.MOTxJ6'
        'wBM7sC0srXmyAAMl9t"Wk4hs2yYTtH0vwUZp4a"WhB2u,o6.!8Zt"'
        "Wf,,eh5tk8WXv9UoM99w2Vr4!.xqA,5MSpWl9p4kJ2oUg'6evkEiQhC'"
        "d5d4k0qA'24nEqhtAQmy37il9p4o8vdoVr!xWSkEDn?,iZpw24kF\"fh"
        "GJZMI8nkI"
    )

    solutions, message = BruteForce.brute_force(encoded_string, ["FURLIN", "BUNKER"])
    print(f"The message is '{message}'.")
    print(f"The settings which worked are: {solutions}.")


if __name__ == "__main__":
    main()
