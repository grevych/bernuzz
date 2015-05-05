# -*- coding: utf-8 -*-

from django.db import models


class Project(models.Model):
    name = models.CharField('Project name', max_length=200)
    description = models.CharField('Project description', max_length=600, blank=True)
    area = models.CharField('Area', max_length=200)
    logo = models.FileField(upload_to='projects/images/', null=True, blank=True)
    parent_id = models.ForeignKey('Project', verbose_name='Parent project', null=True, blank=True)
    team = models.ForeignKey('hierarchy.Team', verbose_name='Team', null=True, blank=True, related_name="projects")
    start_date = models.DateField('Start date', auto_now_add=True)
    end_date = models.DateField('Start date', blank=True, null=True)
    active = models.BooleanField('Active', default=True)
    #status = models.ForeignKey("ProjectStatus", verbose_name="Project Status")
    access_level = models.ForeignKey('AccessLevel', verbose_name="Access Level", null=True, blank=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class ProjectUser(models.Model):
    project = models.ForeignKey('Project', verbose_name='Project', related_name='users')
    user = models.ForeignKey('basic.User', verbose_name='User', related_name='projects')
    #active = models.BooleanField('Active', default=True)
    owner = models.BooleanField('Owner', default=False)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%d: %s -> %s' % (self.pk, self.project.name, self.user, )


class AccessLevel(models.Model):
    name = models.CharField("Access Level", max_length=100)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s' % (self.name)


class ProjectStatus(models.Model):
    name = models.CharField('Project status', max_length=140)
    #project = models.ForeignKey('Project', verbose_name='Project')
    #date
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.name)


class CollegeProject(models.Model):
    project = models.ForeignKey("Project", verbose_name="Project")
    college = models.ForeignKey("College", verbose_name="College")
    date = models.DateField("Added on", auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.college.name)


class ProjectSkill(models.Model):
    skill = models.ForeignKey("Skill", verbose_name="Skill", related_name='projects')
    project = models.ForeignKey("Project", verbose_name="Project", related_name='skills')
    date = models.DateField("Added on", auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.skill.name, self.project.name)


class Skill(models.Model):
    name = models.CharField("Skill Name", max_length=140)
    description = models.CharField("Skill Description", max_length=300)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class Announcement(models.Model):
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
    name = models.CharField('Institution name', max_length=140)
    campus = models.CharField('Campus', max_length=140)
    city = models.CharField('City', max_length=140)
    state = models.CharField('State', max_length=140)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name
