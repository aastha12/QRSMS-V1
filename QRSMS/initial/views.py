import django_filters
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
# Create your views here.
from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from rest_framework import generics, viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.forms.models import model_to_dict
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

from .serializers import (CourseSerializer)
from .serializers import TranscriptSerilazer

from student_portal.models import FeeChallan, Student
from .forms import CourseForm, SemesterForm
from .models import Course, Semester
from .models import MarkSheet


@api_view(['GET'])
def csrf(request):
    return Response({'csrfToken': get_token(request)})

# @login_required(login_url ='/')


def ping(request):
    return JsonResponse({'result': 'OK'})


def index(request):
    return render(request, 'initial/index.html')


def check_if_admin(user):
    return bool(user.is_staff) 


class UserNotLogged(views.APIView):

    def get(self, request):
        return JsonResponse({'message': 'Not Authenticated'}, status=401)


class Add_students(View):
    permission_classes = [IsAdminUser]

    def post(self, request):
        print('Inserting Students')
        from .root_commands import add_students
        students = add_students()
        data = {'List': [x.uid + "," for x in students]}

        return JsonResponse({'status': 'success', **data})


class Add_semesterCore(View):
    @method_decorator(user_passes_test(check_if_admin, login_url='/management/user_not_logged/'))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return JsonResponse({'message': 'Invalid Request'}, status=405)

    def post(self, request):
        print('Inserting Semester')
        semesters = Semester.objects.get(current_semester=True)
        for sem in semesters:
            sem.current_semester = False
            sem.save()
        from .root_commands import add_semesterCore
        data = model_to_dict(add_semesterCore())
        return JsonResponse({'status': 'success', **data})


class Add_university(View):
    def post(self, request):
        print('Inserting University')
        from .root_commands import add_university
        data = model_to_dict(add_university())
        return JsonResponse({'status': 'success', **data})


class Add_superuser(View):
    def post(self, request):
        print('Inserting Superusers')
        from .root_commands import create_super_users
        data = model_to_dict(create_super_users())
        return JsonResponse({'status': 'success', **data})


class Add_courses(View):
    def post(self, request):
        print('Inserting Courses')
        from .root_commands import add_courses
        courses = add_courses()
        data = {'List': [x[1] + "," for x in courses]}
        return JsonResponse({'status': 'success', **data})


class AddCampuses(View):
    def post(self, request):
        from .root_commands import add_campuses

        try:
            data = model_to_dict(add_campuses())
        except IntegrityError as e:
            print(e)
            return JsonResponse({'status': 'success', 'error': 'Campus Already Exists'})
        return JsonResponse({'status': 'success', **data})


class update_challan(View):
    def post(self, request):
        id = request.post['id']
        due_date = request.POST['date']
        admission_fee = request.POST['admission_fee']
        Fine = request.POST['admission_fee']
        withhold = request.POST['withholding']
        other = request.POST['other']
        coactivity = request.POST['coactivity']
        aid = request.POST['aid']
        discount = request.POST['discount']

        challan = FeeChallan.objects.get(student=Student.objects.get(uid=id))
        challan.due_date = due_date
        challan.admission_fee = admission_fee
        challan.Fine = Fine
        challan.withholding_tax = withhold
        challan.other_charges = other
        challan.coActivity_charges = coactivity
        challan.discount = discount
        challan.financial_aid = aid

        challan.total_fee = challan.tution_fee+admission_fee + \
            Fine+withhold+other+coactivity-discount-aid
        challan.Arrears = aid
        challan.save()


class Current_Semester(View):

    def get(self, request):
        semester = Semester.objects.get(current_semester=True)
        return JsonResponse(semester.semester_code, safe=False)


