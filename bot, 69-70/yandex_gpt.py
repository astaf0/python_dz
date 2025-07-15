import requests


class YandexGpt:
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    API_TOKEN = ''
    CATALOG = ''

    def __init__(self):
        self.language = ''
        self.text = ''

    def get_response(self, str):
        payload = {
            "modelUri": f"gpt://{self.CATALOG}/yandexgpt",
            "completionOptions": {
                "stream": False,
                "temperature": 0.4,
                "maxTokens": 100,
                "reasoningOptions": {
                    "mode": "DISABLED"
                }
            },
            "messages": [
                {
                    "role": "user",
                    "text": str,
                }
            ]
        }


        headers = {'Authorization': f"Api-Key {self.API_TOKEN}"}
        res = requests.post(self.url, json=payload, headers=headers)
        answer = res.json()['result']['alternatives'][0]['message']['text']
        return answer