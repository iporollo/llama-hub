# SilverArrow Loader

## Usage

To use this loader, you need to pass in a list of Slack channel ids.

```python
from llama_index import download_loader

SilverArrowReader = download_loader("SilverArrowReader")

loader = SilverArrowReader()
documents = loader.load_data()
```

=
