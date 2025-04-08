from django.shortcuts import render
from django.views.generic import DetailView

from .models import Profile

# Create your views here.
class MyProfile(DetailView):
    model = Profile
    template_name = 'my_profile/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs):
        context = super(MyProfile, self).get_context_data()

        return context
    
    def get_object(self, queryset=None):
        return self.request.user.profile


