from django.shortcuts import render
from year.models import Years


def home_page(request):
    """Display home page."""
    years = []
    for i in Years.objects.all():
        years.append(i.year)
    return render(request, 'index.html', context={'years': years})
