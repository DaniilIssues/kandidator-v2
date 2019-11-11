from django.contrib.auth.decorators import user_passes_test
from django.forms import formset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView

from authapp.models import MyUser
from profile_app.forms import EditForm
from profile_app.models import Account


class BidsView(ListView):
    queryset = Account.objects.all().order_by("-created")
    paginate_by = 30
    template_name = 'adminapp/list_bids_admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(BidsView, self).dispatch(*args, **kwargs)


class EditBidsView(UpdateView):
    model = Account
    form_class = EditForm
    template_name = 'adminapp/update_bids.html'
    success_url = reverse_lazy('staff_profile', kwargs={'page': 1})

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(EditBidsView, self).dispatch(*args, **kwargs)


class UserListView(ListView):
    queryset = MyUser.objects.all().order_by("-date_joined")
    paginate_by = 30
    template_name = 'adminapp/list_users_admin.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(UserListView, self).dispatch(*args, **kwargs)


class EditUserView(UpdateView):
    model = Account
    form_class = EditForm
    template_name = 'adminapp/update_bids.html'

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, *args, **kwargs):
        return super(EditUserView, self).dispatch(*args, **kwargs)
