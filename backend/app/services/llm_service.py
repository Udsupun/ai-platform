import ollama

class LLMService:
    def __init__(self):
        self.client = ollama.Client(
            host="http://ollama:11434"
        )

    def generate_response(
        self,
        prompt: str
    ):
        response = self.client.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
