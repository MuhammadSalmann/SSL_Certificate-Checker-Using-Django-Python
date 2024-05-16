from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .ssl import get_cert_name_from_serial
from .forms import SearchForm


def certificate_view(request):
    serial = request.GET.get("serial", None)
    cert = get_cert_name_from_serial(serial)
    return render(request, "detail.html", context={"cert": cert})


def search_view(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["serial"])
            return redirect(f"/certificate/?serial={form.cleaned_data['serial']}")
    else:
        form = SearchForm()

    return render(request, "search.html", {"form": form})
