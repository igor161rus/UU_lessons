from django.http import HttpResponse


def get_main_page(request):
    return HttpResponse("Это главная страница сайта.")
