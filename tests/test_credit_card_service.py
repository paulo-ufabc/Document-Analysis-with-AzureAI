import pytest
from unittest.mock import MagicMock, patch
from services.credit_card_service import AzureCreditCardService
from models.credit_card_info import CreditCardInfo

@pytest.fixture
def credit_card_service():
    return AzureCreditCardService()

@patch("services.credit_card_service.DocumentIntelligenceClient")
def test_detect_info_success(mock_document_client, credit_card_service):
    # Mock setup
    mock_client_instance = MagicMock()
    mock_document_client.return_value = mock_client_instance
    mock_response = MagicMock()
    mock_client_instance.begin_analyze_document.return_value.result.return_value.documents = [
        MagicMock(fields={
            "CardHolderName": {"content": "John Doe"},
            "CardNumber": {"content": "1234 5678 9012 3456"},
            "ExpiryDate": {"content": "12/25"},
            "BankName": {"content": "Fake Bank"}
        })
    ]

    # Test
    card_url = "https://fakeurl.com/fakeimage.jpg"
    result = credit_card_service.detect_info(card_url)

    # Assert
    expected = CreditCardInfo(
        card_name="John Doe",
        card_number="1234 5678 9012 3456",
        expiry_date="12/25",
        bank_name="Fake Bank"
    )
    assert result == expected

@patch("services.credit_card_service.DocumentIntelligenceClient")
def test_detect_info_failure(mock_document_client, credit_card_service):
    # Mock setup
    mock_client_instance = MagicMock()
    mock_document_client.return_value = mock_client_instance
    mock_client_instance.begin_analyze_document.side_effect = Exception("Analysis error")

    # Test
    card_url = "https://fakeurl.com/fakeimage.jpg"
    result = credit_card_service.detect_info(card_url)

    # Assert
    assert result == CreditCardInfo()
