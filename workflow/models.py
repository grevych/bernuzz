# -*- coding: utf-8 -*-

from django.db import models


class Process(models.Model):
    name = models.CharField('Process name', max_length=140)
    description = models.CharField('Description', max_length=300)
    parent_id = models.ForeignKey('Process', verbose_name='Parent process', blank=True, null=True)
    responsible = models.ForeignKey('basic.User', verbose_name='Responsible', related_name='processes')
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (
        )

    def __unicode__(self):
        return self.name


class ProjectProcess(models.Model):
    project = models.ForeignKey("management.Project", verbose_name="Project", related_name='processes')
    process = models.ForeignKey("Process", verbose_name="Parent Process", related_name='projects')
    date = models.DateField("Added on", auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return "%s - %s" % (self.project.name, self.process.name)


class Stage(models.Model):
    name = models.CharField('Stage name', max_length=100)
    description = models.CharField('Stage description', max_length=200)
    responsible = models.ForeignKey('basic.User', verbose_name='Responsible', related_name='stages')
    process = models.ForeignKey('Process', verbose_name='Process', related_name='stages')
    sub = models.ForeignKey('Process', verbose_name='Sub Process', related_name='parent', blank=True, null=True)
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    due_time = models.DateTimeField('Due time')
    end_time = models.DateTimeField('End date', blank=True, null=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class Task(models.Model):
    description = models.CharField('Task', max_length=300)
    responsible = models.ForeignKey('basic.User', verbose_name='Responsible', related_name='tasks')
    completed = models.BooleanField('Completed', default=False)
    completed_by = models.ForeignKey('basic.User', verbose_name='completed By', related_name='completed', blank=True, null=True)
    stage = models.ForeignKey('Stage', verbose_name='Stage', related_name='tasks')
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    due_time = models.DateTimeField('Due time')
    end_time = models.DateTimeField('End date', blank=True, null=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.description


class StageMessage(models.Model):
    message = models.CharField('Message', max_length=500)
    parent_id = models.IntegerField('In reply to')
    stage = models.ForeignKey('Stage', verbose_name='Stage')
    reply_to = models.ForeignKey('StageMessage', verbose_name='Reply to', null=True)
    date_time = models.DateTimeField('Announcement Date', auto_now_add=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.message


class TaskMessage(models.Model):
    message = models.CharField('Message', max_length=500)
    parent_id = models.IntegerField('In reply to')
    task = models.ForeignKey('Task', verbose_name='Task')
    reply_to = models.ForeignKey('TaskMessage', verbose_name='Reply to', null=True)
    date_time = models.DateTimeField('Announcement date', auto_now_add=True)
    active = models.BooleanField('Active', default=True)

    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.message
