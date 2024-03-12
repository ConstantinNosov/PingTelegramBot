import requests

class TelegramBot:
    def __init__(self, chat_id, bot_token): 
        self.chat_id = chat_id
        self.bot_token = bot_token

    def send_message(self, message):
        """Отправляет сообщение боту."""
        response = requests.get(
            url=f"https://api.telegram.org/bot{self.bot_token}/sendMessage", 
            params={
                'chat_id': self.chat_id,
                'text': message
            }
        )
        return response.json()
