from enum import StrEnum


class Hotel(StrEnum):
    """Habbo hotel domains. Each hotel has its own API origin."""

    COM = "https://www.habbo.com"
    DE = "https://www.habbo.de"
    ES = "https://www.habbo.es"
    FI = "https://www.habbo.fi"
    FR = "https://www.habbo.fr"
    IT = "https://www.habbo.it"
    NL = "https://www.habbo.nl"
    BR = "https://www.habbo.com.br"
    TR = "https://www.habbo.com.tr"

    @property
    def base_url(self) -> str:
        return self.value
