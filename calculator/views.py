from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import BatteryForm, SolarForm, GeneratorForm

def home(request):
    return render(request, 'calculator/home.html')

def battery_size(request):
    result = None
    battery_efficiency=0.8
    if request.method == 'POST':
        form = BatteryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            battery_capacity = (data['daily_energy'] * 1000 * data['days_autonomy']) / \
                              (data['system_voltage'] * data['depth_discharge'] * battery_efficiency)
            result = round(battery_capacity, 2)
    else:
        form = BatteryForm()
    return render(request, 'calculator/battery.html', {'form': form, 'result': result})

def solar_size(request):
    context = {'result': None}
    if request.method == 'POST':
        form = SolarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            solar_wattage = (data['daily_energy'] * 1000) / (data['sun_hours'] * data['system_efficiency'])
            context['result'] = round(solar_wattage, 2)
    else:
        form = SolarForm()
    
    context['form'] = form
    return render(request, 'calculator/solar.html', context)

def generator_size(request):
    results = None
    if request.method == 'POST':
        form = GeneratorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Perform calculations
            generator_size = data['load_power'] * data['safety_factor']
            energy_required = data['load_power'] * data['runtime']
            
            results = {
                'generator_size': round(generator_size, 2),
                'energy_required': round(energy_required, 2)
            }
    else:
        form = GeneratorForm()
    
    return render(request, 'calculator/generator.html', {
        'form': form,
        'results': results
    })
