from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class BatteryForm(forms.Form):
    daily_energy = forms.FloatField(label="Daily Energy Consumption (kWh)", min_value=0.1)
    days_autonomy = forms.FloatField(label="Days of Autonomy", min_value=1)
    system_voltage = forms.FloatField(label="System Voltage (V)", min_value=12)
    depth_discharge = forms.FloatField(label="Depth of Discharge (0.1-1.0)", min_value=0.1, max_value=1.0)

class SolarForm(forms.Form):
    daily_energy = forms.FloatField(
        label="Daily Energy Consumption (kWh)",
        validators=[MinValueValidator(0.1)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
    )
    sun_hours = forms.FloatField(
        label="Average Daily Sun Hours",
        validators=[MinValueValidator(1)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'})
    )
    system_efficiency = forms.FloatField(
        label="System Efficiency",
        validators=[MinValueValidator(0.1), MaxValueValidator(1.0)],
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

class GeneratorForm(forms.Form):
    load_power = forms.FloatField(
        label="Load Power (kW)",
        min_value=0.1,
        max_value=1000,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.1',
            'placeholder': 'Enter load power in kilowatts'
        })
    )
    
    runtime = forms.FloatField(
        label="Required Runtime (hours)",
        min_value=0.5,
        max_value=720,  # 30 days
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.5',
            'placeholder': 'Enter required operation hours'
        })
    )
    
    safety_factor = forms.FloatField(
        label="Safety Factor",
        min_value=1.0,
        max_value=2.5,
        initial=1.2,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'step': '0.1',
            'placeholder': '1.0-2.5 (typical: 1.2)'
        })
    )
