from django.shortcuts import redirect


def redirect_view(request):
    response = redirect('/comment/')
    return response
