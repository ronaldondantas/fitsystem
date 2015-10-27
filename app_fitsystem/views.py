from django.shortcuts import render
from django.utils import timezone
from .models import Student

def student_list(request):
	students = Student.objects.filter(payment_date__lte=timezone.now()).order_by('payment_date')
	return render(request, 'app_fitsystem/student_list.html', {'students' : students})