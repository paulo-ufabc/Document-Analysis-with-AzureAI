from abc import ABC, abstractmethod

class BlobStorageInterface(ABC):
    @abstractmethod
    def upload_file(self, file, file_name: str) -> str:
        pass
