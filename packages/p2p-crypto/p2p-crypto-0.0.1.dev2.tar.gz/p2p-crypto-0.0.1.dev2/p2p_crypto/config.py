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
USER_AGENT = [x[:-1] for x in open(os.path.join(BASE_DIR, 'txt/user-agents.txt'), 'r').readlines()]