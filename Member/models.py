from django.db import models

# Create your models here.
class Member(models.Model):

    class Meta:
        db_table ='member'

    
    member_name=models.CharField(max_length=255)
    member_email = models.EmailField(max_length=255)
    registered_on=models.DateField(auto_now_add=True)
    # quantity=models.IntegerField()
    balance=models.DecimalField(max_digits=11, decimal_places=2,default=0.00, blank=True,null=True)
    # available=models.IntegerField()
    debt=models.DecimalField(max_digits=11,decimal_places=2,default=0.00,blank=True, null=True)

    def __str__(self):
        return self.member_name

    