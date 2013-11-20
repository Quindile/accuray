from django.db import models

class UserData(models.Model):
    eeid = models.CharField("Employee ID", max_length=200)
    username = models.CharField("Username", max_length=200, primary_key=True)
    legal_name = models.CharField("Legal Name", max_length=200)
    fname = models.CharField("First Name", max_length=200)
    lname = models.CharField("Last Name", max_length=200)
    manager = models.CharField("Manager Name", max_length=200)
    l1 = models.CharField("L1 Name", max_length=200)
    l2 = models.CharField("L2 Name", max_length=200)
    l3 = models.CharField("L3 Name", max_length=200)
    email = models.EmailField("Email", max_length=75)
    hire_date = models.DateField('Hire Date')
    job_code = models.CharField("Job Code", max_length=200)
    job_title = models.CharField("Job Title", max_length=200)
    location = models.CharField("Location", max_length=200)
    region = models.CharField("Region", max_length=200)
    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = 'User Data'

class TrainingData(models.Model):
    uname = models.ForeignKey(UserData)
    lp_name = models.CharField("Learning Plan Name", max_length=200)
    item_name = models.CharField("Item Name", max_length=200)
    item_status = models.CharField("Item Status", max_length=200)
    item_type = models.CharField("Item Type", max_length=200)
    hire_date = models.DateField('Hire Date')
    due_date = models.DateField('Due Date')
    def __unicode__(self):
        return self.uname
    class Meta:
        verbose_name_plural = 'Training Data'