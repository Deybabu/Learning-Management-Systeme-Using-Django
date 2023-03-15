from django.shortcuts import render


def welcome_page(request):
    return render(
        request,
        'core/welcome.html',
        context={},
        content_type="text/html"
    )
