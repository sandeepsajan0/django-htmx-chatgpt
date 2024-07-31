from django.shortcuts import render
from django.conf import settings

# from openai import OpenAI
from g4f.client import Client

# client = OpenAI(api_key=settings.OPENAI_API_KEY)
client = Client()


def index(request, *args, **kwargs):
    return render(request, "htmx_chatapp/index.html", context={}, status=200)


def get_messages(request, *args, **kwargs):
    messages = []
    if request.method == "POST":
        question = request.POST.get("question")
        answer = gpt_response(question=question)
        messages = [{"question": question, "answer": answer}]
    return render(request, "partials/message_list.html", context={"messages": messages}, status=200)


def gpt_response(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': question},
        ],
    )
    answer = completion.choices[0].message.content
    return answer
