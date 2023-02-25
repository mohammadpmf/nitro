from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def sign_up_view(request):
    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form })


# این کدها مربوط به مدل کلس بیسد هست.
# from django.views import generic
# from django.urls import reverse_lazy
# class SingUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')