from django.shortcuts import render, get_object_or_404, redirect
from .models import Field, Reservation
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm

def field_list(request):
    fields = Field.objects.all()
    return render(request, 'reservations/field_list.html', {'fields': fields})

@login_required
def create_reservation(request, field_id):
    field = get_object_or_404(Field, id=field_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.field = field
            reservation.save()
            return redirect('reservations:field_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/create_reservation.html', {'form': form, 'field': field})

# Dodane z chatu
def home(request):
    return render(request, 'reservations/home.html')

def about(request):
    return render(request, 'reservations/about.html')

def open_field(request):
    return render(request, 'reservations/open_field.html')

def requirements(request):
    return render(request, 'reservations/requirements.html')

def contact(request):
    return render(request, 'reservations/contact.html')

