from django.shortcuts import render, redirect
from .models import job
from .forms import ListingForms
# Create your views here.
def index(request):
    return render(request, 'webpages/index.html')

def list_jobs(request):
    listing = job.objects.all()
    context = {
        'listing': listing
    }
    return render(request, 'webpages/jobs.html', context)

def retrieve_jobs(request, pk):
    retrieve = job.objects.get(id=pk)
    context = {
        'retrieve': retrieve
    }
    return render(request, 'webpages/ret.html', context)

def listing_create(request):
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


def listing_update(request, pk):
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

def listing_delete(request, pk):
    listing = job.objects.get(id=pk)
    listing.delete()
    return redirect('/jobs')

