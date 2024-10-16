from django import forms
from .models import Contact, Interaction, Event, Task, LineOfBusiness
from .utils import clean_phone_inputs

class NewTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name', 
            'type', 
            'is_follow_up', 
            'line_of_business', 
            'deadline', 
            'description', 
            'time_sensitive', 
            'approval_status'
        ]
        widgets = {
            'type': forms.RadioSelect,
            'line_of_business': forms.CheckboxSelectMultiple,
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea,
            'approval_status': forms.RadioSelect,
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].choices = Task.TASK_TYPE_CHOICES
        self.fields['is_follow_up'].required = False
        self.fields['line_of_business'].queryset = LineOfBusiness.objects.all()
        self.fields['line_of_business'].required = False
        self.fields['time_sensitive'].required = False
        self.fields['approval_status'].choices = [
            ('not_needed', 'Not needed'),
            ('required', 'Approval required')
        ]
        self.fields['approval_status'].initial = 'not_needed'


class NewInteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ['contact', 'type', 'date', 'time', 'description', 'needs_follow_up']
        widgets = {
            'type': forms.RadioSelect,
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact'].queryset = Contact.objects.all().order_by('last_name')
        self.fields['contact'].empty_label = '--- Select a contact ---'
        self.fields['type'].choices = Interaction.CONTACT_TYPE_CHOICES
        self.fields['needs_follow_up'].required = False


class NewContactForm(forms.Form):
    last_name = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=40)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    language = forms.ChoiceField(choices=Contact.LANGUAGE_CHOICES, widget=forms.RadioSelect, initial='english')
    interaction_type = forms.ChoiceField(choices=Interaction.CONTACT_TYPE_CHOICES, widget=forms.RadioSelect)
    interaction_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    interaction_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    interaction_description = forms.CharField(widget=forms.Textarea)
    task_name = forms.CharField(max_length=30)
    task_type = forms.ChoiceField(choices=Task.TASK_TYPE_CHOICES, widget=forms.RadioSelect)
    task_deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    task_description = forms.CharField(widget=forms.Textarea)
    task_urgent = forms.BooleanField(required=False)


    def save(self):
        phone = clean_phone_inputs(self.cleaned_data['phone'])

        contact = Contact.objects.create(
            last_name = self.cleaned_data['last_name'],
            first_name = self.cleaned_data['first_name'],
            phone = phone,
            email = self.cleaned_data['email'],
            tag = 'new_lead',
            language = self.cleaned_data['language'],
        )

        interaction = Interaction.objects.create(
            contact = contact,
            type = self.cleaned_data['interaction_type'],
            date = self.cleaned_data['interaction_date'],
            time = self.cleaned_data['interaction_time'],
            description = self.cleaned_data['interaction_description'],
        )

        Task.objects.create(
            name = self.cleaned_data['task_name'],
            type = self.cleaned_data['task_type'],
            origin = interaction,
            deadline = self.cleaned_data['task_deadline'],
            description = self.cleaned_data['task_description'],
            urgent = self.cleaned_data['task_urgent'],
        )