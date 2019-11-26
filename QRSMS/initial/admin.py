
"""
Admin
"""
from django.contrib import admin
from django_restful_admin import site
from .models import Semester, Course, RegularCoreCourseLoad, RegularElectiveCourseLoad, CourseClass, CourseSection, SectionAttendance, RepeatCourseLoad, CourseSection,CourseClass, CourseStatus, OfferedCourses, AttendanceSheet, MarkSheet


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


site.register(AttendanceSheet)
site.register(MarkSheet)
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