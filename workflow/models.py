# -*- coding: utf-8 -*-

from django.db import models


class Process(models.Model):
    name = models.CharField('Process name', max_length=140)
    description = models.CharField('Description', max_length=300)
    parent_id = models.ForeignKey('Process', verbose_name='Parent process', blank=True, null=True)
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
    responsible = models.IntegerField('Responsible')
    process = models.ForeignKey('Process', verbose_name='Process', related_name='stages')
    start_time = models.DateTimeField('Start time', auto_now_add=True)
    end_time = models.DateTimeField('End date', blank=True, null=True)
    active = models.BooleanField('Active', default=True)
    
    class Meta:
        permissions = (

        )

    def __unicode__(self):
        return self.name


class Task(models.Model):
    description = models.CharField('Task', max_length=300)
    responsible = models.IntegerField('Responsible')
    completed = models.BooleanField('Completed', default=False)
    completed_by = models.IntegerField('Completed by')
    stage = models.ForeignKey('Stage', verbose_name='Stage', related_name='tasks')
    start_time = models.DateTimeField('Start time', auto_now_add=True)
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
