from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from .forms import CustomerUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, CustomUser


class CreateAccountView(CreateView):
    form_class = CustomerUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def form_valid(self, form):
        # Save the user instance
        response = super().form_valid(form)
        # Create a Profile instance for the new user
        Profile.objects.create(user=self.object)
        return response


@login_required
def account_view(request):
    try:
        profile = request.user.profile  
    except Profile.DoesNotExist:
        profile = None

    return render(request, 'account.html', {'profile': profile})


def signup_view(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account')
    else:
        form = CustomerUserCreationForm()

    return render(request, 'news/signup.html', {'form': form})
