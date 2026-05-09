from qdrant_client import QdrantClient
from qdrant_client.models import (Distance, VectorParams, PointStruct)

from sentence_transformers import (SentenceTransformer)

import random

class VectorService:
    def __init__(self):
        self.client = QdrantClient(
            host="qdrant",
            port=6333
        )
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_collection(self):
        collections = (
            self.client.get_collections()
        )

        existing_collections = [
            collection.name
            for collection
            in collections.collections
        ]

        if "notes" not in existing_collections:

            self.client.create_collection(
                collection_name="notes",
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def store_note_embeddings(
        self,
        note_id: int,
        content: str
    ):
        embedding = (
            self.generate_embedding(content)
        )

        self.client.upsert(
            collection_name="notes",
            points=[
                PointStruct(
                    id=note_id,
                    vector=embedding,
                    payload={
                        "content": content
                    }
                )
            ]
        )

    def search_notes(
        self,
        query: str
    ):
        query_embedding = (
            self.generate_embedding(query)
        )

        results = self.client.query_points(
            collection_name="notes",
            query=query_embedding,
            limit=5
        )

        return results

    def generate_embedding(
            self,
            text: str
    ):
        embedding = self.model.encode(
            text
        )

        return embedding.tolist()
