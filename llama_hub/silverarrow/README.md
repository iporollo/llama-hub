# SilverArrow Loader

The SilverArrow Loader returns a set of texts corresponding to embeddings retrieved from the SilverArrow database
The user initializes the loader with a SilverArrow API key and the API url. They then pass in a query vector.

## Usage

```python
from llama_index import download_loader

SilverArrowReader = download_loader("SilverArrowReader")

loader = SilverArrowReader(api_key="YOUR_API_KEY", app_url="YOUR_APP_URL")
documents = loader.load_data()
```

This loader is designed to be used as a way to load data into [LlamaIndex](https://github.com/jerryjliu/gpt_index/tree/main/gpt_index) and/or subsequently used as a Tool in a [LangChain](https://github.com/hwchase17/langchain) Agent. See [here](https://github.com/emptycrown/llama-hub/tree/main) for examples.
