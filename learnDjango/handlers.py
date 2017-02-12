# from django.http import HttpResponse


from django.shortcuts import render
from learnDjango.models import User

# def hello(request):
#     return HttpResponse('<div style=\'background-color:red\'>aaaaaaaa</div>')


def hello(request):
    all_users = User.objects.all()
    print(all_users)
    context = {'hello': 'Hello World! this is in templates', 'all_users': all_users, 'title': 'first sqlite3 in django'}
    return render(request, 'hello.html', context)
