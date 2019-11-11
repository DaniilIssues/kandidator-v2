from django.contrib import auth
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from authapp.forms import LoginForm
from authapp.forms import SignUpForm
from kandidator_v2_0 import settings


def register(request):
    title = 'Регистрация'
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect(reverse("staff_profile", kwargs={'page': 1}))
        else:
            return HttpResponseRedirect(reverse('bids_list_work', kwargs={'pk': request.user.pk, 'page': 1}))

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            account = form.save()
            account.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user.is_superuser:
                reverse_lazy('admin')
            auth.login(request, user)
            send_mail(
                '{}'.format(title),
                'Пользователь с почтой {} и номером {} зарегистрировался'.format(username, request.POST['telephone_num']),
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('create', kwargs={'pk': request.user.pk}))
        else:
            content = {'title': title, 'form': form}
            return render(request, 'authapp/index.html', content)
    else:
        form = SignUpForm()
        content = {'title': title, 'form': form}
        return render(request, 'authapp/index.html', content)


class MyLoginView(LoginView):
    template_name = 'authapp/page-login.html'
    form_class = LoginForm

    def get_success_url(self):
        url = self.get_redirect_url()
        if url:
            return url
        elif self.request.user.is_staff:
            return reverse_lazy("staff_profile", kwargs={'page': 1})
        else:
            return reverse_lazy("bids_list_work", kwargs={'pk': self.request.user.pk, 'page': 1})


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('register')


class ChangePassword(LoginView):
    pass
