from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, Student
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def signup(request):
        if request.method == "POST":
              adminname = request.POST['adminname']
              adminstaffnumber = request.POST['adminstaffnumber']
              adminemail = request.POST['adminemail']
              adminphonenumber = request.POST['adminphonenumber']
              password = request.POST['password']
              confirmpassword = request.POST['confirmpassword']
              institution = request.POST['institution']

              if password == confirmpassword:
                user = Member.objects.create(adminname=adminname, adminstaffnumber=adminstaffnumber, adminemail=adminemail, adminphonenumber=adminphonenumber, institution=institution) # Use set_password to securely hash and save the password.
                user.save()
                messages.success(request, 'Registration successful. You can now login.')
                return redirect("dashboard")
              else:
                messages.error(request, 'Passwords do not match.')
                context = {}
                return render(request, 'signup.html', context)
        else:
             context = {}
             return render(request, 'signup.html', context)
        
def register(request):
    if request.method == 'POST':
        admission_number = request.POST['admisionnumber']
        full_name = request.POST['fullname']
        course_of_study = request.POST['courseofstudy']
        duration_of_study = request.POST['duration']
        mode_of_study = request.POST['mode']
        
        # Create a new Student object and save it to the database
        student = Student(admission_number=admission_number,full_name=full_name,course_of_study=course_of_study,duration_of_study=duration_of_study,mode_of_study=mode_of_study)
        student.save()
        return redirect('/success/')
    return render(request, 'registration_form.html')

# def progress(request):
#     if request.method == 'POST':
#         student = Student.objects.get(id=request.POST['student_id'])
#         units = Unit.objects.filter(id__in=request.POST.getlist('units'))

#         for unit in units:
#             registration = Registration(student=student, unit=unit)
#             registration.save()

#             for semester in range(1, student.years_of_study + 1):
#                 for attempt in range(1, 4):
#                     examination = Examination(registration=registration, semester=semester, attempt=attempt)
#                     examination.save()

#                     if examination.passed:
#                         break

#                 result = Result(registration=registration, gpa=calculate_grade_point(examination.marks))
#                 result.save()

#         gpa = get_average_gpa(student)
#         if gpa >= 2.0:
#             student.progress += 1
#             student.save()

#     return render(request, 'your_template.html')


# def login(request):
#     if request.method == 'POST':
#         adminstaffnumber = request.POST['adminstaffnumber']
#         password = request.POST['password']
#         user = authenticate(adminstaffnumber=adminstaffnumber, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'welcome user')
#             return render(redirect, "dashboard")
#         else:
#             messages.error(request, "User doesnt exist")
#             return render(request, 'login.html')
#     return render(request, 'login.html')
        
#def login(request):
#    if request.method == 'POST':
#        adminstaffnumber = request.POST.get('adminstaffnumber')
#        password = request.POST.get('password')
#        Member = authenticate(request, adminstaffnumber=adminstaffnumber, password=password)
#        if Member is not None:
#            login(request, Member)
#            messages.success(request, 'Welcome user')
#            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
#        else:
#            error_message = "Invalid credentials. Please try again."
#            messages.error(request, error_message)
#            return render(request, 'login.html', {'error_message': error_message})
#    
#    return render(request, 'login.html')


def loginview(request):
    if request.method == 'POST':
        adminstaffnumber = request.POST.get('adminstaffnumber')
        password = request.POST.get('password')

        try:
            user = Member.objects.get(adminstaffnumber=adminstaffnumber)
            login(request, user)  # Django's login function automatically handles password verification
            messages.success(request, 'Welcome user')
            return redirect('dashboard')  # Replace 'dashboard' with your actual dashboard URL name
        except Member.DoesNotExist:
            error_message = "User not found. Please try again."
            messages.error(request, error_message)
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')




def dashboard(request):
  template = loader.get_template('dashboard.html')
  return HttpResponse(template.render())

def manage(request):
  template = loader.get_template('manage.html')
  return HttpResponse(template.render())

def results(request):
  template = loader.get_template('results.html')
  return HttpResponse(template.render())



def datab(request):
    data = Member.objects.all()
    context = {'data':data}
    template = loader.get_template('manage.html')
    return HttpResponse(template.render(context))


        # Create a new user
        

        # Log the user in
        

        # Redirect the user to the home page
        
    
        
        