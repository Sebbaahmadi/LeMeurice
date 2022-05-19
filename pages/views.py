from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'page//home.html')

def about(request):
    return render(request, 'page//about.html')

# {Changed the name of the function to Contact to avoid collision}
def contact(request):
   # templates = 'contact.html'
    if request.method == 'POST':
        # part 1 take data from the form .
        v_n = request.POST.get('name')
        v_e = request.POST.get('email')
        v_s = request.POST.get('subject')
        v_m = request.POST.get('message')
        # part 2 create a object of the class contact.
        c = Contact(name=v_n, email=v_e, subject=v_s, massage=v_m)
        # part 3 save the object in the database.
        c.save()
        # part 4 return the message to the user.
        return render(request, 'page/thanks.html')
    else:

        return render(request, 'page/contact.html')




