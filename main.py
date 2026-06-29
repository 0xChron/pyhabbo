"""Quick smoke script — prefer pytest and the README examples for real usage."""

from pyhabbo import HabboClient, Hotel


def main() -> None:
    with HabboClient(hotel=Hotel.COM) as client:
        client.ping()
        print("ping OK")

if __name__ == "__main__":
    main()
