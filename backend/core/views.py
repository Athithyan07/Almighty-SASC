from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import ChatMessage

@require_http_methods(["GET"])
def get_chat_history(request):
    messages = ChatMessage.objects.order_by('timestamp')[:50] # Get last 50 messages
    history = []
    for message in messages:
        history.append({
            'sender': 'Anonymous',
            'content': message.content,
            'timestamp': message.timestamp.isoformat()
        })
    return JsonResponse({'history': history})

@require_http_methods(["POST"])
def send_chat_message(request):
    data = json.loads(request.body)
    message_content = data.get('message')
    if not message_content:
        return JsonResponse({'message': 'Message content cannot be empty'}, status=400)

    # Assuming a default sender or anonymous user for now
    # You might need to adjust this based on how you handle users without authentication
    ChatMessage.objects.create(content=message_content)
    return JsonResponse({'message': 'Message sent and saved'}, status=201)
