from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Client
from .models import Client
from .forms import ClientForm, EquipmentForm, StaffForm, TestimonialForm
from .models import Client, Equipment, Staff, Testimonial,DrillingRequest
from .forms import DrillingRequestForm,ProjectForm,Project



# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def products(request):
    return render(request,'products.html')
def store(request):
    return render(request,'store.html')
def dashboard(request):
    requests = DrillingRequest.objects.all()
    return render(request,'dashboard.html', {'requests':requests})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'register.html', {'form':form})
def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name ,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})

def dashboard(request):
    return render(request, 'dashboard.html')

def clients_view(request):
    return render(request, 'clients.html')

def drilling_requests_view(request):
    return render(request, 'drilling_requests.html')

def equipment_view(request):
    return render(request, 'equipment.html')

def projects_view(request):
    return render(request, 'projects.html')

def staff_view(request):
    return render(request, 'staff.html')

def testimonials_view(request):
    return render(request, 'testimonials.html')

def testimonial_form_view(request):
    return render(request, 'testimonial_form.html')
#new codes
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients')
    else:
        form = ClientForm()
    return render(request, 'add_client.html', {'form': form})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'add_equipment.html', {'form': form})

def add_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'add_staff.html', {'form': form})

def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'testimonial_form.html', {'form': form})
#client_lists
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})
#new edits
# def dashboard(request):
#     return render(request, 'dashboard.html')
#
# def client_list(request):
#     clients = Client.objects.all()
#     return render(request, 'clients.html', {'clients': clients})
#
def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment.html', {'equipment': equipment})
#
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff.html', {'staff': staff})
#
def project_list(request):
    return render(request, 'projects.html')

def drilling_requests(request):
    Drill = DrillingRequest.objects.all()
    return render(request, 'drilling_requests.html',{'Drill': Drill})


def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})
def add_drilling_request(request):
    if request.method == 'POST':
        form = DrillingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drilling_requests')  # or redirect wherever you want
    else:
        form = DrillingRequestForm()
    return render(request, 'add_drilling_request.html', {'form': form})
#add project
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
from .models import Client, Equipment, Staff, Project, DrillingRequest, Testimonial

def dashboard(request):
    total_clients = Client.objects.count()
    total_equipment = Equipment.objects.count()
    total_staff = Staff.objects.count()
    total_projects = Project.objects.count()
    total_requests = DrillingRequest.objects.count()
    total_testimonials = Testimonial.objects.count()

    context = {
        'total_clients': total_clients,
        'total_equipment': total_equipment,
        'total_staff': total_staff,
        'total_projects': total_projects,
        'total_requests': total_requests,
        'total_testimonials': total_testimonials,
    }

    return render(request, 'dashboard.html', context)



