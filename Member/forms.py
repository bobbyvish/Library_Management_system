from django import forms
from .models import Member

class MemberForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        
    class Meta:
        model= Member
        fields=['member_name','member_email','balance']

    member_name= forms.CharField(label='Name',max_length=255)
    member_email= forms.EmailField(label='EmailId',max_length=255)
    balance=forms.FloatField(label='Paid')
    

    # def clean_member_email(self):
    #     email= self.cleaned_data['member_email']
    #     if not self.instance and Member.objects.filter(member_email=email).exists():
    #         raise forms.ValidationError('Email of Member already exist!')
    #     return email