import requests

from app.services.base_summarizer_service import BaseSummarizerService


class RemoteSummarizerService(BaseSummarizerService):
    host = "https://api-inference.huggingface.co/"
    model = "models/IlyaGusev/mbart_ru_sum_gazeta"

    def __init__(self, api_token):
        # Подготовка сервиса к работе: сохранение токена и урла модели
        self.api_token = api_token
        self.api_url = f"{self.host}{self.model}"

    def summarize(self, text):
        headers = {"Authorization": f'Bearer {self.api_token}'}

        def query(payload):
            response = requests.post(self.api_url,
                                     headers=headers,
                                     json=payload)
            return response.json()

        output = query({
            "inputs": text,
        })

        return output[0]['summary_text']
