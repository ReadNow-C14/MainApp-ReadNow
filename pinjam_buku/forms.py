from django.forms import ModelForm
from pinjam_buku.models import BorrowedBook

class BorrowForm(ModelForm):
    class Meta:
        model = BorrowedBook
        fields = ['return_date']