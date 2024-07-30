from django.shortcuts import render


def index(request, *args, **kwargs):
    if request.method == 'post':
        return render(request, 'htmx_chatapp/index.html', context={}, status=200)
    return render(request, 'htmx_chatapp/index.html', context={}, status=200)


