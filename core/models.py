from django.db import models


class LineOfBusiness(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Line of Business"
        verbose_name_plural = 'Lines of Business'



class Task(models.Model):
    TASK_TYPE_CHOICES = {
        'call': 'Call',
        'email': 'Email',
        'proposal': 'Prepare proposal',
        'handle': 'Handle something else'
    }

    APPROVAL_STATUS_CHOICES = {
        'not_needed': 'Not needed',
        'required': 'Required',
        'approved': 'Approved'
    }

    name = models.CharField(max_length=60)
    type = models.CharField(max_length=15, choices=TASK_TYPE_CHOICES)
    is_follow_up = models.BooleanField(default=False)
    line_of_business = models.ManyToManyField(LineOfBusiness, blank=True)
    origin = models.ForeignKey('Interaction', on_delete=models.CASCADE)
    deadline = models.DateField()
    description = models.TextField(blank=True)
    time_sensitive = models.BooleanField(default=False)
    approval_status = models.CharField(max_length=15, choices=APPROVAL_STATUS_CHOICES, default='not_needed')
    result = models.TextField(blank=True)
    done = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name} ({self.type}) - From {self.origin}'


class Event(models.Model):
    EVENT_TYPE_CHOICES = {
        'appointment': 'Appointment',
        'expected_call': 'Expected call'
    }

    origin = models.ForeignKey('Interaction', on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=EVENT_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField(blank=True)
    did_it_happen = models.BooleanField(default=False)


class Interaction(models.Model):
    CONTACT_TYPE_CHOICES = {
        'call': 'Call',
        'email': 'Email',
        'appointment': 'Appointment',
        'walk_in': 'Walk-in'
    }

    contact = models.ForeignKey('Contact', on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=CONTACT_TYPE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    needs_follow_up = models.BooleanField(default=False)
    result = models.TextField(blank=True)

    def __str__(self):
        return f'{self.contact} - {self.type} ({self.date})' 


class Contact(models.Model):
    TAG_CHOICES = {
        'new_lead': 'New Lead',
        'ex_client': 'Ex-Client',
        'client': 'Client'
    }

    LANGUAGE_CHOICES = {
        'engish': 'English',
        'spa_pref': 'Spanish preferred',
        'spanish': 'Just Spanish'
    }

    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, null=True)
    tag = models.CharField(max_length=18, choices=TAG_CHOICES)
    language = models.CharField(max_length=18, choices=LANGUAGE_CHOICES, default='english') #This should be a model to be able to customize it
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'               