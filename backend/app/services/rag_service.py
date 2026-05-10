from app.services.llm_service import LLMService
from app.services.vector_service import VectorService


class RAGService:
    def __init__(self, vector_service: VectorService, llm_service: LLMService):
        self.vector_service = vector_service
        self.llm_service = llm_service

    def ask_question(self, question: str, user_id: int):
        results = self.vector_service.search_notes(question, user_id)

        context = "\n".join([result.content for result in results])

        prompt = f"""Answer the question using the context below:

        Context:
        {context}

        Question:
        {question}
        """

        return self.llm_service.generate_response(prompt)
