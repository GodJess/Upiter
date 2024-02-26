from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Messenger
import json
from django.conf import settings
from .serializers import SerlMessage

class MessengerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass  # Пока что не намерены что-то делать при отключении

    async def receive(self, text_data):
        data = json.loads(text_data)
        await sync_to_async(self.save_message)(data)

    async def save_message(self, data):
        text = data.get('text')
        date = data.get('date')
        time = data.get('time')
        sender = data.get('sender')
        recipient = data.get('recipient')

        message = Messenger.objects.create(sender=sender, recipient=recipient, message=text, date=date, time=time)
        message.save()

        messages_from_sender = SerlMessage(Messenger.objects.filter(sender=sender, recipient=recipient).values(), many = True)
        messages_to_recipient = SerlMessage(Messenger.objects.filter(sender=recipient, recipient=sender).values(), many = True)

        message = {
            'message_send_user': messages_from_sender.data,   
            'message_get_user': messages_to_recipient.data
        }

        await self.send(text_data=json.dumps(message))
    


