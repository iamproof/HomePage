from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import Info, InfoForm


@login_required
def index(request):
	return render(request, 'accounts/index.html')

@login_required
def edit(request):
	if request.method == "POST":
		# form = InfoForm(request.POST or None, instance=info)
		form = InfoForm(request.POST)
		# edit_profile_form = EditProfileForm(request.POST or None,
        # current_user=request.user, instance=profile)
		
		if form.is_valid():
			user = User.objects.get(username=request.user)
			info, created = Info.objects.get_or_create(user=user)
			info.birth_year = form.cleaned_data["birth_year"]
			info.favorite_music = form.cleaned_data["favorite_music"]
			info.favorite_colors = form.cleaned_data["favorite_colors"]
			info.sex  = form.cleaned_data["sex"]
			info.about = form.cleaned_data["about"]
			info.favorite_sports = ", ".join(form.cleaned_data["favorite_sports"])
			info.save()
			return render(request, 'accounts/index.html')

		return render(request, 'blog/index.html')

	return render(request, 'accounts/edit.html', {'form': InfoForm()})
