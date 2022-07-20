from django.shortcuts import render, redirect
from .models import job #importing models
from .forms import ListingForms # importing forms
# Create your views here. explaing functions based view
def index(request):
    return render(request, 'webpages/index.html') #home page view

def list_jobs(request):
    listing = job.objects.all()
    context = {
        'listing': listing
    }
    return render(request, 'webpages/jobs.html', context) # listing view

def retrieve_jobs(request, pk): # retrieve view
    retrieve = job.objects.get(id=pk)
    context = {
        'retrieve': retrieve
    }
    return render(request, 'webpages/ret.html', context)

def listing_create(request): # create view
    form = ListingForms()
    if request.method == 'POST':
        form =ListingForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'forms': form
    }
    return render(request, 'webpages/create.html', context)


def listing_update(request, pk): # update view
    updates = job.objects.get(id=pk)
    form = ListingForms(instance = updates)

    if request.method == 'POST':
        form =ListingForms(request.POST, instance = updates)
        if form.is_valid():
            form.save()
            return redirect('/jobs')
    
    context = {
        'forms': form
    }
    return render(request, 'webpages/update.html', context)

def listing_delete(request, pk): # list view
    listing = job.objects.get(id=pk)
    listing.delete()
    return redirect('/jobs')

