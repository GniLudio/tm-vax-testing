from django.http import HttpResponse

# Create your views here.
def dummy_view(request):
    return HttpResponse("This is the dummy view.")