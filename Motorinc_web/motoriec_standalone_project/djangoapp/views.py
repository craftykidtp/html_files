from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import SignUpForm
from .models import Spare


@login_required
def home(request):
    return render(request, "index.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created. You can now log in.")
            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, "registration/register.html", {"form": form})


@login_required
def spares(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        category = request.POST.get("category", "").strip()
        price_text = request.POST.get("price", "").strip()
        stock = request.POST.get("stock", "").strip()

        try:
            price = float(price_text)
            if price < 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "Enter a valid price equal to or greater than zero.")
        else:
            if not name or not category or not stock:
                messages.error(request, "Please complete all the spare-part fields.")
            else:
                Spare.objects.create(
                    name=name,
                    category=category,
                    price=price,
                    stock=stock,
                )
                messages.success(request, "Spare part added successfully.")
                return redirect("spares")

    spare_list = Spare.objects.all().order_by("id")
    return render(request, "spares.html", {"spares": spare_list})


@login_required
def contact(request):
    return render(request, "contact.html")


@login_required
@require_POST
def delete(request, id):
    spare = get_object_or_404(Spare, id=id)
    spare.delete()
    messages.success(request, "Spare part deleted.")
    return redirect("spares")


@login_required
def edit(request, id):
    spare = get_object_or_404(Spare, id=id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        category = request.POST.get("category", "").strip()
        price_text = request.POST.get("price", "").strip()
        stock = request.POST.get("stock", "").strip()

        try:
            price = float(price_text)
            if price < 0:
                raise ValueError
        except (TypeError, ValueError):
            messages.error(request, "Enter a valid price equal to or greater than zero.")
        else:
            if not name or not category or not stock:
                messages.error(request, "Please complete all the spare-part fields.")
            else:
                spare.name = name
                spare.category = category
                spare.price = price
                spare.stock = stock
                spare.save()
                messages.success(request, "Spare part updated successfully.")
                return redirect("spares")

    return render(request, "edit.html", {"spare": spare})
