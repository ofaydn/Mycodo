# -*- coding: utf-8 -*-
#
# forms_manual_measurements.py - Manual Measurements Flask Forms
#


from flask_babel import lazy_gettext
from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import DateTimeField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms import widgets
from wtforms.widgets import NumberInput
from wtforms import DecimalField
#from wtforms import validators
from wtforms import StringField

from mycodo.config_translations import TRANSLATIONS


#
# Manual Measurements
#
    
class NoteAdd(FlaskForm):
    name = StringField(
        TRANSLATIONS['name']['title'])
    #note_tags = SelectMultipleField('Tags')
    #files = FileField(lazy_gettext('Attached Files'))
    enter_custom_date_time = BooleanField(lazy_gettext('Use Custom Date/Time'))
    date_time = DateTimeField(
        'Custom Date/Time', format='%Y-%m-%d %H:%M:%S')
    note = TextAreaField(TRANSLATIONS['note']['title'])
    value = DecimalField(
        TRANSLATIONS['value']['title'],
        widget=NumberInput(step='any')
    )
    note_add = SubmitField(TRANSLATIONS['save']['title'])


class NoteOptions(FlaskForm):
    note_unique_id = StringField(widget=widgets.HiddenInput())
    note_mod = SubmitField(TRANSLATIONS['edit']['title'])
    note_del = SubmitField(TRANSLATIONS['delete']['title'])


class NoteMod(FlaskForm):
    note_unique_id = StringField(widget=widgets.HiddenInput())
    #file_selected = StringField(widget=widgets.HiddenInput())
    name = StringField(TRANSLATIONS['name']['title'])
    #note_tags = SelectMultipleField(lazy_gettext('Tags'))
    #files = FileField(lazy_gettext('Attached Files'))
    enter_custom_date_time = BooleanField(lazy_gettext('Use Custom Date/Time'))
    date_time = DateTimeField('Custom Date/Time', format='%Y-%m-%d %H:%M:%S')
    note = TextAreaField(TRANSLATIONS['note']['title'])
    value = DecimalField(
        TRANSLATIONS['value']['title'],
        widget=NumberInput(step='any')
    )
    #file_del = SubmitField(TRANSLATIONS['delete']['title'])
    note_cancel = SubmitField(TRANSLATIONS['cancel']['title'])
    rename_name = StringField()
    #file_rename = SubmitField(TRANSLATIONS['rename']['title'])
    note_del = SubmitField(TRANSLATIONS['delete']['title'])
    note_save = SubmitField(TRANSLATIONS['save']['title'])


