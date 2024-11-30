from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from interfaces.document_analysis_interface import DocumentAnalysisInterface
from utils.config import Config
from models.credit_card_info import CreditCardInfo
from utils.logger import setup_logger

logger = setup_logger()

class AzureCreditCardService(DocumentAnalysisInterface):
    def __init__(self):
        self.client = DocumentIntelligenceClient(Config.ENDPOINT, AzureKeyCredential(Config.KEY))

    def detect_info(self, card_url: str) -> CreditCardInfo:
        try:
            response = self.client.begin_analyze_document("prebuilt-creditCard", {"urlSource": card_url})
            result = response.result()
            for document in result.documents:
                fields = document.fields
                return CreditCardInfo(
                    card_name=fields.get("CardHolderName", {}).get("content"),
                    card_number=fields.get("CardNumber", {}).get("content"),
                    expiry_date=fields.get("ExpiryDate", {}).get("content"),
                    bank_name=fields.get("BankName", {}).get("content")
                )
        except Exception as e:
            logger.error(f"Erro ao analisar o cartão de crédito: {e}")
            return CreditCardInfo()
