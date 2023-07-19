"""SilverArrow Reader."""

from typing import Any, List
from llama_index.readers.base import BaseReader
from llama_index.schema import Document


class SilverArrowReader(BaseReader):
    """SilverArrow reader."""

    def __init__(self):
        """Initialize with parameters."""
        import silverarrow

    def load_data(self, *args: Any, **load_kwargs: Any) -> List[Document]:
        return super().load_data(*args, **load_kwargs)
