
"""
Admin
"""
from django.contrib import admin
from django_restful_admin import site
from django.db import models
from advanced_filters.admin import AdminAdvancedFiltersMixin
from .models import Semester, Course, StudentMarks, Transcript, RegularCoreCourseLoad, RegularElectiveCourseLoad, SectionAttendance, RepeatCourseLoad, CourseSection, CourseClass, CourseStatus, OfferedCourses, AttendanceSheet, MarkSheet, StudentAttendance, StudentInfoSection, SectionMarks


admin.site.site_title = "UMSRA Admin Portal"
admin.site.register(RegularCoreCourseLoad)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(RegularElectiveCourseLoad)
admin.site.register(CourseClass)
admin.site.register(CourseSection)
admin.site.register(SectionAttendance)
admin.site.register(RepeatCourseLoad)
admin.site.register(OfferedCourses)
admin.site.register(CourseStatus)
admin.site.register(AttendanceSheet)
admin.site.register(MarkSheet)
admin.site.register(StudentAttendance)
admin.site.register(StudentInfoSection)
admin.site.register(Transcript)

site.register(StudentInfoSection)
site.register(StudentAttendance)
site.register(AttendanceSheet)
admin.site.register(StudentMarks)
site.register(MarkSheet)
admin.site.register(SectionMarks)
site.register(OfferedCourses)
site.register(CourseStatus)
site.register(RepeatCourseLoad)
site.register(RegularElectiveCourseLoad)
site.register(Semester)
site.register(RegularCoreCourseLoad)
site.register(Course)
site.register(CourseClass)
site.register(CourseSection)
site.register(SectionAttendance)
