from django.shortcuts import render, redirect
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def single_slug(request , single_slug):
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories :
        matching_series =TutorialSeries.objects.all().filter(Category__slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(Tutorial_Series__Series=m.Series).earliest("Date_Published")
            series_urls[m] = part_one.Tutorial_slug

        return render(request=request,
                      template_name='categorys.html',
                      context={"Series": matching_series, "part_ones": series_urls})


    tutorials = [t.Tutorial_slug for  t in Tutorial.objects.all()]
    if single_slug in tutorials :
        return HttpResponse(f'hey {single_slug} is a tutorial !!! ')


    
    return HttpResponse('sorry boddy there is no such category!!!')
    

def page(request):
    return render(request = request,
                  template_name='Category.html',
                  context = {"categories":TutorialCategory.objects.all})


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'you loged in {username}')
            messages.info(request, f'you logged in as {username}')

            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})




def logout_request(request):
  logout(request)
  messages.info(request, f'Logged out')
  return redirect('home')

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})