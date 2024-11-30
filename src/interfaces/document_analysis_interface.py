from abc import ABC, abstractmethod
from models.credit_card_info import CreditCardInfo

class DocumentAnalysisInterface(ABC):
    @abstractmethod
    def detect_info(self, card_url: str) -> CreditCardInfo:
        pass
