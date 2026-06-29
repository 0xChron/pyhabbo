from enum import StrEnum


class Hotel(StrEnum):
    """Habbo hotel API origins. Each member is the full base URL."""

    COM = "https://www.habbo.com"
    DE = "https://www.habbo.de"
    ES = "https://www.habbo.es"
    FI = "https://www.habbo.fi"
    FR = "https://www.habbo.fr"
    IT = "https://www.habbo.it"
    NL = "https://www.habbo.nl"
    BR = "https://www.habbo.com.br"
    TR = "https://www.habbo.com.tr"
