from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    PointStruct,
    VectorParams,
)
from sentence_transformers import SentenceTransformer

from app.utils.text_chunker import chunk_text


class VectorService:
    def __init__(self):
        self.client = QdrantClient(host="qdrant", port=6333)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_collection(self):
        collections = self.client.get_collections()

        existing_collections = [
            collection.name for collection in collections.collections
        ]

        if "notes" not in existing_collections:

            self.client.create_collection(
                collection_name="notes",
                vectors_config=VectorParams(size=384, distance=Distance.COSINE),
            )

    def store_note_embeddings(self, note_id: int, content: str, user_id: int):
        chunks = chunk_text(content)
        points = []
        for chunk in chunks:
            embedding = self.generate_embedding(chunk)
            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=embedding,
                    payload={"user_id": user_id, "note_id": note_id, "content": chunk},
                )
            )

        self.client.upsert(collection_name="notes", points=points)

    def search_notes(self, query: str, user_id: int):
        query_embedding = self.generate_embedding(query)

        results = self.client.query_points(
            collection_name="notes",
            query=query_embedding,
            query_filter=Filter(
                must=[FieldCondition(key="user_id", match=MatchValue(value=user_id))]
            ),
            limit=5,
        )

        return [
            {
                "score": result.score,
                "note_id": result.payload["note_id"],
                "content": result.payload["content"],
            }
            for result in results.points
        ]

    def generate_embedding(self, text: str):
        embedding = self.model.encode(text)

        return embedding.tolist()
