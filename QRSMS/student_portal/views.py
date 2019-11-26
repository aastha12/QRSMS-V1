from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from rest_framework import generics, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test

from actor.models import CURRENT_SEMESTER, CURRENT_SEMESTER_CODE, ordered_to_dict
from .serializers import StudentSerializer


from .forms import StudentForm, StudentFormValidate
from .models import Student

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class UserNotLogged(View):
    def get(self, request):
        return JsonResponse({'message':'Not Authenticated'}, status=401)

def check_if_student(user):
    return True if user.is_student else False

class Home_json(View):
        
    def get(self, request):
        print(dir(request))
        data_dict = model_to_dict(Student.objects.filter(uid = request.user).first())
        user_data = model_to_dict(request.user)
        user_data.pop('groups',None)
        user_data.pop('password', None)
        print(data_dict)
        print(user_data)
        dat = {'status':'success',**data_dict,**user_data}
        
        return JsonResponse(dat)
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        

class BaseStudentLoginView(View):
    @method_decorator(login_required)
    @method_decorator(user_passes_test(check_if_student))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AttendanceView(BaseStudentLoginView):
    def get(self, request, course_code):
        from initial.models import AttendanceSheet, OfferedCourses
        print(dir(self))
        print(dir(request.user))
        s = Student.objects.get(uid = request.user)
        csddc = course_code + "_" + s.semester_code
        at = AttendanceSheet.objects.get(student__uid = request.user, scsddc__endswith = csddc)
        
        from initial.serializers import AttendanceSheetSerializer
        att_serialized = AttendanceSheetSerializer(at, many = True).data

        return JsonResponse({'message':'Available Attendacne','condition':True, 'attendance':att_serialized}, status=200)

class TimeTableView(BaseStudentLoginView):
    def get(self, request):
        import requests
        uid = str(request.user)
        city = uid[2].lower()
        rnum = uid[4:]
        year = uid[0:2]
        url = 'https://timetablenotifier.com/api/fetch.php?email="'+ str(city+year+rnum) +'@nu.edu.pk"'
        print(url)
        r = requests.get(url)
        data = r.json()    
        return JsonResponse(data)
class RegistrationCheck(BaseStudentLoginView):
    def get(self, request):
        print(request.user)
        from institution.models import Department, Degree
        try:
            s = Student.objects.get(uid = request.user)
            
            dep = Department.objects.get(department_students = s)
            deg = Degree.objects.get(degree_short = s.degree_short_enrolled, offering_department = dep)


        except Degree.DoesNotExist as e:
            return JsonResponse({'message':'Invalid Student. Degree Does not Exist','condition':True, 'error_raised':True}, status=401)

        except Department.DoesNotExist as e:
            return JsonResponse({'message':'Invalid Student. Department Does not Exist','condition':True, 'error_raised':True}, status=401)

        if dep is None or deg is None:
            return JsonResponse({'message':'Invalid Student','condition':True}, status=401)

        if(deg.registrations_open == True):
            return JsonResponse({'message' : 'Regisrations are Active', 'condition':True},status=200)    
        else:
            return JsonResponse({'message' : 'Regisrations are NOT Active', 'condition':False},status=200)  

class RegistrationCourses(BaseStudentLoginView):
    def get(self, request):
        from institution.models import Department, Degree
        try:
            s = Student.objects.get(uid = request.user)
            if s.warning_count > 0:
                return JsonResponse({'message':'Student in Warning. Conatact Academic Office.','condition':False}, status=200)
            from initial.models import Semester, OfferedCourses
            # sem = Semester.objects.get(semester_code=CURRENT_SEMESTER_CODE)
            # rg_courses = sem.regular_course_load.get(semester_season=CURRENT_SEMESTER,student_year=s.student_year)
            # el_courses = sem.elective_course_load.get(semester_season=CURRENT_SEMESTER)

            s = OfferedCourses.objects.filter(student__uid=str(request.user))
        
            from rest_framework.request import Request

            from initial.serializers import OfferedCoursesSerializer
            offered_courses_to_student = OfferedCoursesSerializer(s, many = True, context = {'request': Request(request)}).data

            from pprint import pprint
            pprint(offered_courses_to_student)
            
        except Semester.DoesNotExist as e:
            return JsonResponse({'message':'Invalid Semester. Contact Adminstration.','condition':False, 'error_raised':True}, status=401)

        except OfferedCourses.DoesNotExist as e:
            return JsonResponse({'message':'Invalid Student. Department Does not Exist','condition':False, 'error_raised':True}, status=401)

        if offered_courses_to_student is None:
            return JsonResponse({'message':'No Available Courses','condition':False}, status=401)

        return JsonResponse({'message':'Available Courses','condition':True, 'regular_courses':offered_courses_to_student}, status=200)
        

class StudentSignupView(View):
    def post(self, request):
        form = StudentFormValidate(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return JsonResponse({'status':"Success", 'message':'Student Sign Up Successful.'})
        else:
            return JsonResponse(form.errors.get_json_data())

class StudentLoginView(View):

    def get(self, request,*args, **kwargs):
        return HttpResponse("PLease Login" + str(kwargs))

    def post(self, request,*args,**kwargs):
        username = request.POST['username']
        password = request.POST['password']
        if username is "" or password is "":
            return HttpResponse(content="Empty Usename or Password Field.", status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            dict_user = model_to_dict(user)
            dict_user.pop('groups',None)
            dict_user.pop('password', None)
            return JsonResponse({'status':'success','message' : 'User Logged In', **dict_user})
        else:
            return JsonResponse({'status':"Invalid Username of Password."}, status = 403)
        
        return HttpResponseRedirect('/home')

class StudentLogoutView(View):
    def post(self, request):
        logout(request)
        return JsonResponse({'status':'success','message' : 'User Logged Out'})

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentListView(ListView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm


def email(request):
    subject = 'GPA Warning Alert'
    message = "Dear Student, this is to inform you that your Progress "
    message += "has not been very satisfactory in last semester and your GradePoints are below 2.0."
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]
    send_mail(subject, message, email_from, recipient)
    return HttpResponse({"Status":"Success"})