from app.services.llm_service import LLMService
from app.services.vector_service import VectorService

class RAGService:
    def __init__(self):
        self.vector_service = VectorService()
        self.llm_service = LLMService()

    def ask_question(
        self,
        question: str
    ):
        results = self.vector_service.search_notes(question)

        context = "\n".join([
            result.payload["content"]
            for result in results.points
        ])

        prompt = f"""Answer the question using the context below:

        Context:
        {context}

        Question:
        {question}
        """

        return self.llm_service.generate_response(prompt)
