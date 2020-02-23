from django.db import models

# Create your models here.


class Hospital(models.Model):
    hospital_id =models.AutoField(primary_key=True)
    hospital_name =models.CharField(max_length=100,null=False)
    created_date =models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Hospital"

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100,null=False)
    company_email=models.CharField(max_length=100)
    created_date =models.DateTimeField(auto_now=True)
    startd_ate = models.DateTimeField(null=False)
    class Meta:
        db_table = "Company"


class Plans(models.Model):
    plan_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    premium = models.DecimalField(decimal_places=4,max_digits=18)
    sum_assured = models.DecimalField(decimal_places=4,max_digits=18)
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,null=True)
    created_date =models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    class Meta:
        db_table = "Plans"

class Benifits(object):
    benifit_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    percent_no_claim_bonus = models.DecimalField(max_length=100,decimal_places=4,max_digits=7,null=True)
    restoration_amount = models.DecimalField(decimal_places=4,max_digits=18,null=True)
    min_claimed_range =models.DecimalField(decimal_places=4,max_digits=18)
    plan_id = models.ForeignKey(Plans,on_delete=models.CASCADE,null=True)
    is_active = models.BooleanField()
    class Meta:
        db_table = "Benifits"

class Member(models.Model):
    member_id =models.AutoField(primary_key=True)
    member_name =models.CharField(max_length=100)
    date_of_birth= models.DateTimeField(null=True)
    contact_details = models.IntegerField()
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(null=True)
    class Meta:
        db_table = "Member"

class Policy(models.Model):
    policy_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(null=True)
    is_renewed= models.BooleanField()
    total_amount_canclaim= models.DecimalField(decimal_places=4,max_digits=18)
    issued_date = models.DateTimeField(null=True)
    inception_date=models.DateTimeField(null=True)
    expiry_date=models.DateTimeField(null=False)
    plan_id= models.ForeignKey(Plans,on_delete=models.CASCADE,null=False)
    member_id = models.ForeignKey(Member,on_delete=models.CASCADE,null=False)
    class Meta:
        db_table = "Policy"


class Claim(models.Model):
    claim_id = models.AutoField(primary_key=True)
    is_closed= models.BooleanField(null=True)
    is_cancelled = models.BooleanField(null=True)
    is_approved = models.BooleanField(null=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(null=True)
    pretreatment_date = models.DateTimeField(null=True)
    pretreatment_amount = models.DecimalField(decimal_places=4,max_digits=18,null=True)
    postreatment_amount = models.DecimalField(decimal_places=4,max_digits=18,null=True)
    posttreatment_date = models.DateTimeField(null=True)
    is_paid = models.BooleanField()
    class Meta:
        db_table = "Claim"

class Treatment(models.Model):
    treatment_id = models.AutoField(primary_key=True)
    claim_id = models.ForeignKey(Claim,on_delete=models.CASCADE,null=False)
    hospital_id = models.ForeignKey(Hospital,on_delete=models.CASCADE,null=False)
    admission_date = models.DateField(null=False)
    discharge_date = models.DateField(null=False)
    treatment_cost = models.DecimalField(decimal_places=4,max_digits=18,null=True)
    class Meta:
        db_table = "Treatment"

class ClaimSettlementinfo(models.Model):
    claimsettlement_id = models.AutoField(primary_key=True)
    claim_id = models.ForeignKey(Claim,on_delete=models.CASCADE,null=False)
    claim_settlement_amount = models.DecimalField(decimal_places=4,max_digits=18,null=True)
    claim_settlement_date = models.DateTimeField(auto_now=True)
    is_claimfullypaid = models.BooleanField(null= True)
    class Meta:
        db_table = "ClaimSettlementinfo"

class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)

class Customer(models.Model):
    customer_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,null=False)
    emails= models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=100,null=False)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=False)
    



    

    





