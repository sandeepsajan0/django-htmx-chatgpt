from django.shortcuts import render
from django.conf import settings

# from openai import OpenAI
from g4f.client import Client

from .models import ChatMessage

# client = OpenAI(api_key=settings.OPENAI_API_KEY)
client = Client()


def index(request, *args, **kwargs):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = gpt_response(question=question)
        chat = ChatMessage.objects.create(question=question, answer=answer)
        return render(request, "partials/message_list.html", context=chat.message, status=200)
    messages = ChatMessage.objects.all()
    return render(request, "htmx_chatapp/index.html", context={"messages": messages}, status=200)


def gpt_response(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': question},
        ],
    )
    answer = completion.choices[0].message.content
    return answer
