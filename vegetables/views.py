from vegetables.models import Vegetable

from django.views import View

from django.views import generic

from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile

from vegetables.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from vegetables.forms import CreateForm

class VegetableListView(OwnerListView):

    model = Vegetable

    template_name = "vegetables/vegetable_list.html"


class VegetableDetailView(OwnerDetailView):

    model = Vegetable

    template_name = "vegetables/vegetable_detail.html"


class VegetableCreateView(LoginRequiredMixin, View):

    model = Vegetable

#    fields = ['title', 'price', 'text']

    template = "vegetables/vegetable_form.html"

    success_url = reverse_lazy('vegetables:all')
    def get(self, request, pk=None) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # add owner to the model before saving
        vegetable = form.save(commit=False)
        vegetable.owner = self.request.user
        vegetable.save()
        return redirect(self.success_url)


class VegetableUpdateView(LoginRequiredMixin, View):

    model = Vegetable

 #   fields = ['title', 'price', 'text']

    template = "vegetables/vegetable_form.html"

    success_url = reverse_lazy('vegetables:all')
    def get(self, request, pk) :
        vegetable = get_object_or_404(Vegetable, id=pk, owner=self.request.user)
        form = CreateForm(instance=vegetable)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        vegetable = get_object_or_404(Vegetable, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=vegetable)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        vegetable = form.save(commit=False)
        vegetable.save()

        return redirect(self.success_url)



class VegetableDeleteView(OwnerDeleteView):

    model = Vegetable

    template_name = "vegetables/vegetable_delete.html"

def stream_file(request, pk) :
    vegetable = get_object_or_404(Vegetable, id=pk)
    response = HttpResponse()
    response['Content-Type'] = vegetable.content_type
    response['Content-Length'] = len(vegetable.picture)
    response.write(vegetable.picture)
    return response

