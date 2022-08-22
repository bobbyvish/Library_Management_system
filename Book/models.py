from django.db import models
from Member.models import Member
# Create your models here.
class Book(models.Model):

    class Meta:
        db_table ='book'

    
    title=models.TextField()
    author = models.TextField()
    publisher=models.CharField(max_length=255)
    # quantity=models.IntegerField()
    isbn=models.CharField(max_length=255)
    # available=models.IntegerField()
    quantity=models.CharField(max_length=255, default=1)
    book_stock=models.IntegerField(default=0)
    rented= models.IntegerField(default=0)

    def __str__(self):
        return self.title



class Transaction(models.Model):

    class Meta:
        db_table = 'transaction'

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date= models.DateField(auto_now_add=True)
    return_date= models.DateField(null=True)
    total_days= models.IntegerField(default=0)
    total_charge=models.DecimalField(max_digits=11, decimal_places=2,default=0.00)
    amount_paid= models.DecimalField(max_digits=11, decimal_places=2, default=0.00)

    def calculate_total_days(self):
        return (self.return_date - self.borrow_date).days + 1
    
    def calculate_total_charge(self):
        return float(self.total_days) * 10.00

    def calculate_amount_paid(self):
        return float(self.total_days) * 10.00

    