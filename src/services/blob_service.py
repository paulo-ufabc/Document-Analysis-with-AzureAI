from azure.storage.blob import BlobServiceClient
from interfaces.blob_storage_interface import BlobStorageInterface
from utils.config import Config
from utils.logger import setup_logger

logger = setup_logger()

class AzureBlobService(BlobStorageInterface):
    def __init__(self):
        self.client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        self.container_name = Config.CONTAINER_NAME

    def upload_file(self, file, file_name: str) -> str:
        try:
            blob_client = self.client.get_blob_client(container=self.container_name, blob=file_name)
            blob_client.upload_blob(file, overwrite=True)
            logger.info(f"Arquivo '{file_name}' enviado com sucesso.")
            return blob_client.url
        except Exception as e:
            logger.error(f"Erro ao enviar o arquivo '{file_name}': {e}")
            return None
