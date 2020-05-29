from django.conf import settings
from .constants import ACTION_PAY, CURRENCY_UAH

LIQPAY_PUBLIC_KEY = getattr(settings, 'LIQPAY_PUBLIC_KEY', '')
LIQPAY_PRIVATE_KEY = getattr(settings, 'LIQPAY_PRIVATE_KEY', '')
LIQPAY_DEFAULT_CURRENCY = getattr(settings, 'LIQPAY_DEFAULT_CURRENCY',
                                  CURRENCY_UAH)
LIQPAY_DEFAULT_LANGUAGE = getattr(settings, 'LIQPAY_DEFAULT_LANGUAGE', 'ru')
LIQPAY_DEFAULT_ACTION = getattr(settings, 'LIQPAY_DEFAULT_ACTION', ACTION_PAY)
LIQPAY_SANDBOX = getattr(settings, 'LIQPAY_SANDBOX', 0)
LIQPAY_CONF = getattr(settings, 'LIQPAY_CONF', {})
DEFAULT_LIQPAY = getattr(settings, 'DEFAULT_LIQPAY', 'default')
ADDITIONAL_LIQPAY = getattr(settings, 'ADDITIONAL_LIQPAY', 'additional')
