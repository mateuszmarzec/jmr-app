from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView

from shortener.models import LongUrl


class IndexView(CreateView):
    template_name = 'index.html'
    model = LongUrl
    fields = ['url']

    def form_valid(self, form):
        shortener = LongUrl.objects.get_or_create(url=form.cleaned_data['url'])[0]
        context = self.get_context_data()
        context.update({'shortcut': shortener.shortcut, 'host': self.request.META['HTTP_HOST']})
        return render(self.request, self.template_name, context)


class RedirectView(TemplateView):
    def get(self, request, *args, **kwargs):
        shortener = get_object_or_404(LongUrl, shortcut=kwargs['shortcut'])
        return redirect(shortener.url)
