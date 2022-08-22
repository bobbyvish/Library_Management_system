from django import forms
from .models import Book  

class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

   
    class Meta:
        model = Book
        fields =['title','author','publisher','isbn','quantity']
                
    title=forms.CharField(label='Title', max_length=255, required=False)
    author=forms.CharField(label='Author',max_length=255, required=False)
    publisher=forms.CharField(label='Publisher',max_length=255, required=False)
    isbn=forms.CharField(label='isbn',required=False)
    quantity=forms.CharField(label='Quantity',required=False)

    def clean_title(self):
        title=self.cleaned_data['title']
        if str(self.instance)== '' and Book.objects.filter(title=title).exists():
            raise forms.ValidationError(' Book title already Exist')
        return title
    






