# -*- coding: utf-8 -*-

from django.db import models


class Project(models.Model):
    name = models.CharField('Project name', max_length=200, unique=True)
    description = models.CharField('Project description', max_length=600, blank=True)
    area = models.CharField('Area', max_length=200)
    logo = models.CharField('Project logo', max_length=140, blank=True)
    parent_id = models.ForeignKey('Project', verbose_name='Parent project', null=True, blank=True)
    team = models.ForeignKey('hierarchy.Team', verbose_name='Team', null=True, blank=True)
    start_date = models.DateField('Start date', auto_now_add=True)
    end_date = models.DateField('Start date', blank=True, null=True)
    active = models.BooleanField('Active', default=True)

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


class ProjectPrivacy(models.Model):
    name = models.CharField('Project privacy', max_length=100)
    project = models.ForeignKey('Project', verbose_name='Project')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.name)


class ProjectStatus(models.Model):
    name = models.CharField('Project status', max_length=140)
    project = models.ForeignKey('Project', verbose_name='Project')
    #date
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.name)


class CollegeProject(models.Model):
    project = models.ForeignKey('Project', verbose_name='Project')
    college = models.ForeignKey('College', verbose_name='College')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.college.name)


class ProjectSkill(models.Model):
    skill = models.ForeignKey('Skill', verbose_name='Skill')
    project = models.ForeignKey('Project', verbose_name='Project')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.skill.name, self.project.name)


class ProjectProcess(models.Model):
    project = models.ForeignKey('Project', verbose_name='Project')
    process = models.ForeignKey('workflow.Process', verbose_name='Process')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return '%s - %s' % (self.project.name, self.process.name)


class Skill(models.Model):
    name = models.CharField('Skill name', max_length=140)
    description = models.CharField('Skill description', max_length=300)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class Announcement(models.Model):
    subject = models.CharField('Subject', max_length=140)
    message = models.CharField('Message', max_length=500)
    date_time = models.DateTimeField('Announcement date', auto_now_add=True)
    active = models.BooleanField('Active', default=True)

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
