from pyhabbo import HabboClient, Hotel


def main() -> None:
    client = HabboClient(hotel=Hotel.COM)
    client.ping()
    print("ping OK")


if __name__ == "__main__":
    main()
