from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponseRedirect
from .forms import UploadForm
from .models import Profile


class ProfileView(View):

    def get(self, request: HttpRequest):
        form = UploadForm()
        return render(request, 'accounts/profile_me.html', {'form': form})

    def post(self, request: HttpRequest):
        profile, created = Profile.objects.get_or_create(user=request.user)
        form = UploadForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
