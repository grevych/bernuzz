from django.db import models


class Project(models.Model):
    name = models.CharField("Project Name", max_length=200)
    area = models.CharField("Area", max_length=200)
    logo = models.CharField("Project Logo", max_length=140, blank=True)
    parent_id = models.ForeignKey("Process", verbose_name="Parent Process", null=True)
    start_date = models.DateField("Start Date", auto_now_add=True)
    end_date = models.DateField("Start Date", blank=True, null=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class ProjectPrivacy(models.Model):
    name = models.CharField("Project Privacy", max_length=100)
    project = models.ForeignKey("Project", verbose_name="Project")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permission = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.project.name, self.name)


class ProjectStatus(models.Model):
    name = models.CharField("Project Status", max_length=140)
    project = models.ForeignKey("Project", verbose_name="Project")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.project.name, self.name)


class CollegeProjects(models.Model):
    project = models.ForeignKey("Project", verbose_name="Project")
    college = models.ForeignKey("College", verbose_name="College")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.project.name, self.college.name)


class ProjectSkills(models.Model):
    skill = models.ForeignKey("Skills", verbose_name="Skill")
    project = models.ForeignKey("Project", verbose_name="Project")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.skill.name, self.project.name)


class ProjectProcesses(models.Model):
    project = models.ForeignKey("Project", verbose_name="Project")
    process = models.ForeignKey("workflow.Process", verbose_name="Process")
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.project.name, self.process.name)


class Skills(models.Model):
    name = models.CharField("Skill Name", max_length=140)
    description = models.CharField("Skill Description", max_length=300)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class Announcements(models.Model):
    subject = models.CharField("Subject", max_length=140)
    message = models.CharField("Message", max_length=500)
    date_time = models.DateTimeField("Announcement Date", auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.subject


class College(models.Model):
    name = models.CharField("Institution Name", max_length=140)
    campus = models.CharField("Campus", max_length=140)
    city = models.CharField("City", max_length=140)
    state = models.CharField("State", max_length=140)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name
