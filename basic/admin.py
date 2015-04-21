from django.contrib import admin
from basic.models import Member
from hierarchy.models import Team, TeamMember, Role
from workflow.models import Process, ProjectProcess, Task, Stage, TaskMessage, StageMessage
from management.models import Project, ProjectPrivacy, ProjectSkill, ProjectStatus, College, CollegeProject, Skill, \
    Announcement
# Register your models here.

admin.site.register(Member)
admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Role)
admin.site.register(Process)
admin.site.register(ProjectProcess)
admin.site.register(Task)
admin.site.register(Stage)
admin.site.register(TaskMessage)
admin.site.register(StageMessage)
admin.site.register(Project)
admin.site.register(ProjectPrivacy)
admin.site.register(ProjectSkill)
admin.site.register(ProjectStatus)
admin.site.register(College)
admin.site.register(CollegeProject)
admin.site.register(Skill)
admin.site.register(Announcement)


