import os

paymentTypes = {
    'Юmoney'          : 'YandexMoneyNew', 
    'Тинькофф'        : 'TinkoffNew', 
    'Росбанк'         : 'RosBankNew', 
    'Райффайзен'      : 'RaiffeisenBank', 
    'QIWI'            : 'QIWI', 
    'МТС банк'        : 'MTSBank', 
    'Home Credit'     : 'HomeCreditBank', 
    'BinancePay (RUB)': 'RUBfiatbalance', 
    'Почта банк'      : 'PostBankNew', 
    'Payeer'          : 'Payeer', 
    'Уралсиб'         : 'UralsibBank', 
    'АК Барс'         : 'AkBarsBank', 
    'Мобильный'       : 'Mobiletopup', 
    'Advcash'         : 'Advcash', 
    'БКС'             : 'BCSBank', 
    'Реннесанс'       : 'RenaissanceCredit', 
    'Русский стандарт': 'RussianStandardBank', 
    'Банк Петербург'  : 'BankSaintPetersburg', 
    'ОТП'             : 'OTPBankRussia', 
    'Юникредит'       : 'UniCreditRussia', 
    'Европа кредит'   : 'CreditEuropeBank', 
    'Ситибанк'        : 'CitibankRussia', 
    'Альфа'           : 'ABank', 
    'Cash'            : 'CashInPerson'
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from p2p_crypto import user_agent
USER_AGENT=user_agent.USER_AGENT