ACTION_PAY = 'pay'
ACTION_HOLD = 'hold'
ACTION_SUBSCRIBE = 'subscribe'
ACTION_PAYDONATE = 'paydonate'
ACTION_AUTH = 'auth'

ACTIONS = (
    (ACTION_PAY, ACTION_PAY),
    (ACTION_HOLD, ACTION_HOLD),
    (ACTION_SUBSCRIBE, ACTION_SUBSCRIBE),
    (ACTION_PAYDONATE, ACTION_PAYDONATE),
    (ACTION_AUTH, ACTION_AUTH),
)

CURRENCY_UAH = 'UAH'
CURRENCY_USD = 'USD'
CURRENCY_EUR = 'EUR'
CURRENCY_BYN = 'BYN'
CURRENCY_KZT = 'KZT'
CURRENCY_RUB = 'RUB'

CURRENCIES = (
    (CURRENCY_UAH, CURRENCY_UAH),
    (CURRENCY_USD, CURRENCY_USD),
    (CURRENCY_EUR, CURRENCY_EUR),
    (CURRENCY_BYN, CURRENCY_BYN),
    (CURRENCY_KZT, CURRENCY_KZT),
    (CURRENCY_RUB, CURRENCY_RUB),
)

API_VERSION = '3'
CHECKOUT_URL = '3/checkout/'