"""GET /api/public/ping — health check."""

from pyhabbo import HabboClient


def main() -> None:
    client = HabboClient()
    client.ping()
    print("API is reachable")


if __name__ == "__main__":
    main()
