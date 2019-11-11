from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.timezone import now
from django.views.generic import DetailView, UpdateView, CreateView, ListView
from profile_app.forms import EditForm
from profile_app.models import BidModel, Account


# Вынес пагинацию в отдельную функцию во избежание повторения кода
def paginate(objects, pages, num_page):
    paginator = Paginator(objects, pages)
    try:
        bids_pages = paginator.page(num_page)
        return bids_pages
    except PageNotAnInteger:
        bids_pages = paginator.page(1)
        return bids_pages
    except EmptyPage:
        bids_pages = paginator.page(paginator.num_pages)
        return bids_pages


@login_required
def create_bid(request, pk):
    title = 'Новая заявка'
    if request.method == 'POST':
        form = EditForm(request.POST)
        if form.is_valid():
            account = form.save()
            account.user = request.user
            account.move = True
            account.created = now()
            account.save()
            send_mail(
                '{}'.format(title),
                'Пользователь с почтой {} создал заявку id {}'.format(request.user.username, account.pk),
                '{}'.format(request.user.username),
                ['to@example.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('bids_list_work', kwargs={'pk': request.user.pk, 'page': 1}))
        else:
            content = {'title': title, 'form': form}
            return render(request, 'profile_app/create-form.html', content)
    else:
        form = EditForm()
        content = {'title': title, 'form': form}
        return render(request, 'profile_app/create-form.html', content)


# Реаоизация изменеия форм без ajax
class EditBidView(UpdateView):
    model = Account
    form_class = EditForm
    template_name = 'profile_app/includes/ajax_form.html'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True

    def form_valid(self, form):
        data = Account.objects.get(pk=self.kwargs['pk'])
        acc = form.save()
        acc.created = data.created
        acc.move = True
        acc.save()
        return super(EditBidView, self).form_valid(form)

    def get_success_url(self):
        url = str(self.request.headers['referer'])
        page = int(url.split('/')[-2])
        return reverse_lazy('bids_list_work', kwargs={'pk': self.request.user.pk, 'page': page})


@login_required
def bid_list_in_work_view(request, pk, page=1):
    title = 'Заявки в работе'
    bids = Account.objects.filter(user=pk).exclude(status="AR").order_by('-created')
    bids_pages = paginate(bids, 30, page)
    in_work = True
    content = {
        'objects': bids_pages,
        'title': title,
        'in_work': in_work,
    }

    return render(request, 'profile_app/list_bids.html', content)


@login_required
def bid_list_in_archive_view(request, pk, page=1):
    title = 'Архив заявок'
    bids = Account.objects.filter(user=pk, status='AR')
    bids_pages = paginate(bids, 30, page)
    in_work = False
    content = {
        'objects': bids_pages,
        'title': title,
        'in_work': in_work,
    }

    return render(request, 'profile_app/list_bids.html', content)


@login_required
def stop_work(request, pk):
    text = 'Заявка приостановлена'
    url = request.headers['referer']
    bids = Account.objects.get(pk=pk)
    bids.status = "ST"
    bids.move = False
    bids.save()
    send_mail(
        '{}'.format(text),
        'Пользователь с почтой {} приостановил заявку id{}'.format(request.user, bids.pk),
        '{}'.format(request.user.username),
        ['to@example.com'],
        fail_silently=False,
    )
    return redirect(url)


@login_required
def play_work(request, pk):
    text = 'Заявка возобновлена'
    url = request.headers['referer']
    bids = Account.objects.get(pk=pk)
    bids.status = "ON"
    bids.move = True
    bids.save()
    # send_mail(
    #     '{}'.format(text),
    #     'Пользователь с почтой {} возобновил заявку id{}'.format(request.user, bids.pk),
    #     '{}'.format(request.user.username),
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
    return redirect(url)

# Ajax realisation
