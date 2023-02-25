from django.shortcuts import render, redirect
from django.contrib.auth import forms

def sign_up_view(request):
    if request.method=='POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = forms.UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form })


# این کدها مربوط به مدل کلس بیسد هست.
# from django.views import generic
# from django.contrib.auth import forms
# from django.urls import reverse_lazy

# class SignUpView(generic.CreateView):
#     form_class = forms.UserCreationForm
#     template_name = 'registration/signup.html'
#     success_url = reverse_lazy('login')