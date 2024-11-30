import pytest
from unittest.mock import MagicMock, patch
from services.blob_service import AzureBlobService

@pytest.fixture
def blob_service():
    return AzureBlobService()

@patch("services.blob_service.BlobServiceClient")
def test_upload_file_success(mock_blob_service_client, blob_service):
    # Mock setup
    mock_blob_client = MagicMock()
    mock_blob_service_client.from_connection_string.return_value.get_blob_client.return_value = mock_blob_client
    mock_blob_client.url = "https://fakeaccount.blob.core.windows.net/container/fakefile.jpg"

    # Test
    mock_file = MagicMock()
    file_name = "fakefile.jpg"
    result = blob_service.upload_file(mock_file, file_name)

    # Assert
    assert result == "https://fakeaccount.blob.core.windows.net/container/fakefile.jpg"
    mock_blob_client.upload_blob.assert_called_once_with(mock_file, overwrite=True)

@patch("services.blob_service.BlobServiceClient")
def test_upload_file_failure(mock_blob_service_client, blob_service):
    # Mock setup
    mock_blob_service_client.from_connection_string.return_value.get_blob_client.side_effect = Exception("Connection error")

    # Test
    mock_file = MagicMock()
    file_name = "fakefile.jpg"
    result = blob_service.upload_file(mock_file, file_name)

    # Assert
    assert result is None
