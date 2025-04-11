from django import forms
from .models import Client, Equipment, Staff, Testimonial
from .models import DrillingRequest
from .models import Project


class ClientForm(forms.ModelForm):
        class Meta:
            model = Client
            fields = ['name', 'email', 'location', 'phone']  # ← add phone here

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'start_date', 'end_date', 'progress', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'status']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'role']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'message']


class DrillingRequestForm(forms.ModelForm):
    class Meta:
        model = DrillingRequest
        fields = ['client', 'location', 'depth_required', 'status']

