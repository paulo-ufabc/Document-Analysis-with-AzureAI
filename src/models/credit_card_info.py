from dataclasses import dataclass

@dataclass
class CreditCardInfo:
    card_name: str = None
    card_number: str = None
    expiry_date: str = None
    bank_name: str = None
