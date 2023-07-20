"""SilverArrow Reader."""

from typing import Any, List
from llama_index.readers.base import BaseReader
from llama_index.schema import Document


class SilverArrowReader(BaseReader):
    """SilverArrow reader."""

    def __init__(self, api_key: str, app_url: str):
        """SilverArrow reader.

        Args:
            api_key (str): SilverArrow API key.
            app_url (str): SilverArrow instance url.
        """
        import silverarrow

        self._client = silverarrow.SilverArrowAPI(api_key, app_url)

    def load_data(
        self,
        query_vector: Any,
        limit: int = 10,
    ) -> List[Document]:
        """Load data from SilverArrow.

        Args:
            query_vector (Any): Query
            limit (int): Number of results to return.

        Returns:
            List[Document]: A list of documents.

        """

        results = self._client.search(query_vector, limit)

        documents = []
        for result in results:
            document = Document(
                doc_id=result["id"],
                score=result["score"],
                document=result["document"],
            )
            documents.append(document)

        return documents
