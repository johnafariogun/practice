from django.forms import ModelForm
from .models import job


class ListingForms(ModelForm):
    class Meta:
        model = job
        fields = [
            'name',
            'job_type',
            'description',
            'contacts',
            'publish',
            'created',
            'updated',
        ]