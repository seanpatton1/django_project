from django.http import HttpResponse

# Create your views here.

def about_me(request):
    
    if request.method == "POST":
        return("You must have POSTed something")
    else:
        return HttpResponse(request.method)