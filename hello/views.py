from django.shortcuts import render


def hello(request):
    name = request.GET.get('name', '')
    message = request.GET.get('message', '')
    context = {'name': name, 'message': message}
    return render(request, 'mainpage.html', context)
