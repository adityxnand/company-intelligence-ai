from langchain_openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

import os
load_dotenv()

def get_embedding_model():
    embedding_model = OpenAIEmbeddings(
    api_key=os.getenv("JINA_API_KEY"),
    model="jina-embeddings-v5-text-small",
    base_url="https://api.jina.ai/v1",
    check_embedding_ctx_length=False
    )

    return embedding_model

_model = None

def _get_model():
    """Load the model once, on first use."""
    global _model
    if _model is None:
        _model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    return _model

def embed_texts(texts: list[str]) -> list[list[float]]:
    model = _get_model()
    vectors = model.encode(texts, batch_size=64, normalize_embeddings=True)
    return vectors.tolist()