# from django.http import HttpResponse


from django.shortcuts import render

# def hello(request):
#     return HttpResponse('<div style=\'background-color:red\'>aaaaaaaa</div>')


def hello(request):
    context          = {}
    context['hello'] = 'Hello World! this is in templates'
    return render(request, 'hello.html', context)
