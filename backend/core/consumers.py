import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from .models import ChatMessage # Import ChatMessage model

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # Send list of teacher users to the frontend
        teacher_users = User.objects.filter(role='teacher').values('id', 'username')
        self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': list(teacher_users)
        }))

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']

        # Assuming user is authenticated and available in scope
        user = self.scope['user']
        if user.is_authenticated:
            # Save message to database
            ChatMessage.objects.create(sender=user, content=message_content)

        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'sender': user.username,
            'message': message_content
        }))