from django.shortcuts import render

def student_list(request):
    return render(request, 'app_fitsystem/student_list.html', {})