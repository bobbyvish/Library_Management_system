from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .models import Member
from .forms import MemberForm
from django.db.models import Q
from Book.models import Transaction

# Add Member view
class MemberCreateView(View):

    template_name = 'member.html'
    context={}

    def get(self, request):

        form= MemberForm() 

        #checking get method for search from search button attr name=searchdata
        #if search is not pass then show all record
        if 'searchdata' in request.GET:
            search=request.GET.get('search')
            # search filter for member base on name and email
            members=Member.objects.filter(Q(member_name__icontains=search)
                                        | Q(member_email__icontains=search))
        else:
            members=Member.objects.all() # fetching record from database to show 
       
       #passing form, member and url in context
        self.context.update({
            'title': 'Add Member',
            'form': form,
            'members': members,
            'url': reverse('members')
        })
        return render(request, self.template_name, self.context)

    def post(self, request):

        form=MemberForm(request.POST)

        if not form.is_valid():
            self.context.update({
                'title': 'Add Member',
                'form': form,
            })
            messages.warning(request, "Some field is Invalid")
            return render(request, self.template_name, self.context)
            
        email=form.cleaned_data['member_email']

        # condition for checking unique email
        if Member.objects.filter(member_email=email).exists():
            messages.warning(request, "Email Already exists")
            return redirect(reverse('members'))
        form.save()
        
        messages.success(request, "Member Created Successfully")
        return redirect(reverse('members'))


#Update Member data
class MemberEditView(View):

    template_name="update_form.html"
    context={'title':'Update Member'}

    def get(self, request, id):

        try:
            member_id = Member.objects.get(pk=id)   # getting data from model through id
        except Member.DoesNotExist:
            messages.error(request, "Member record does not exist")
            return render(request, self.template_name)

        
        #fetching form instance and showing at form to update
        form= MemberForm(instance=member_id)

        self.context.update({
            'url': reverse('memberedit',kwargs={'id':id}), #passing url and id for form action url 
            'member_id': member_id,
            'form': form,
        })
        return render(request, self.template_name, self.context)

    def post(self, request, id):

        try:
            member_id = Member.objects.get(pk=id)    # getting data from model through id
        except Member.DoesNotExist:
            messages.error(request, "Member record does not exist")
            return render(request, self.template_name)
        
        form = MemberForm(request.POST, instance=member_id) 
        if not form.is_valid():
            self.context.update(
                            {
                            'form':form
                            })
            return render(request,self.template_name,self.context)
        
        member=form.save(commit=False)  #using commit false so that update some form field instance before saving

        #logic for updating balance and debt of member  before updating the data in database
        #if balance is update in form then balance is calulate based on the debt of member
        if member.balance >= member.debt:
            member.balance -= member.debt
            member.debt=0.00
        else:
            member.debt -= member.balance
            member.balance=0.00
        member.save()

        messages.success(request,"Member Record is successfully updated")
        return redirect(reverse("members"))

#Delete Member View
class MemberDeleteView(View):
    def get(self, request, id):

        try:
            member_id = Member.objects.get(pk=id)
        except Member.DoesNotExist:
            messages.warning(request, "Member record does not exist")
            return redirect(reverse("members"))
        
        #checking if member is rented book then don't allow to delete member Record
        #login is if member id is present and return data is null in transaction table means member not returned the book 
        if Transaction.objects.filter(member=id ,return_date__isnull=True):
            messages.success(request, "Book is Rented to this member, Record can't be deleted")
            return redirect(reverse("members"))

        member_id.delete()
        messages.success(request, "Member record deleted successfully")
        return redirect(reverse("members"))

