# -*- coding: utf-8 -*-
import glob
import logging
import os
import time
from datetime import datetime

from flask import url_for

from mycodo.config_translations import TRANSLATIONS
from mycodo.databases import set_uuid
from mycodo.databases.models import ManualMeasurements
from mycodo.mycodo_flask.extensions import db
from mycodo.mycodo_flask.utils.utils_general import delete_entry_with_id
from mycodo.mycodo_flask.utils.utils_general import flash_success_errors

logger = logging.getLogger(__name__)


#
# ManualMeasurements
#

def note_add(form):
    action = '{action} {controller}'.format(
        action=TRANSLATIONS['add']['title'],
        controller=TRANSLATIONS['manual measurements']['title'])
    error = []

    new_note = ManualMeasurements()

    if not form.name.data:
        error.append("Name cannot be left blank")
    if not form.value.data:
        error.append("Value cannot be left blank")


    if form.enter_custom_date_time.data:
        try:
            new_note.date_time = datetime_time_to_utc(form.date_time.data)
        except Exception as msg:
            error.append("Error while parsing date/time: {}".format(msg))

    if not error:
        new_note.unique_id = set_uuid()
        new_note.name = form.name.data
        new_note.note = form.note.data
        new_note.value = form.value.data
        new_note.save()

    flash_success_errors(error, action, url_for('routes_page.page_manual_measurements'))


def note_mod(form):
    action = '{action} {controller}'.format(
        action=TRANSLATIONS['modify']['title'],
        controller=TRANSLATIONS['manual measurements']['title'])
    error = []

    mod_note = ManualMeasurements.query.filter(
        ManualMeasurements.unique_id == form.note_unique_id.data).first()

    if not form.name.data:
        error.append("Name cannot be left blank")
    if not form.value.data:
        error.append("Value cannot be left blank")

    try:
        mod_note.date_time = datetime_time_to_utc(form.date_time.data)
    except:
        error.append("Error while parsing date/time")

    if not error:
        mod_note.name = form.name.data
        mod_note.note = form.note.data
        mod_note.value = form.value.data
        db.session.commit()

    flash_success_errors(error, action, url_for('routes_page.page_manual_measurements'))


def note_del(form):
    action = '{action} {controller}'.format(
        action=TRANSLATIONS['delete']['title'],
        controller=TRANSLATIONS['manual measurements']['title'])
    error = []

    if not form.note_unique_id.data:
        error.append("Unique id is empty")

    if not error:
        delete_entry_with_id(ManualMeasurements, form.note_unique_id.data)

    flash_success_errors(error, action, url_for('routes_page.page_manual_measurements'))


def datetime_time_to_utc(datetime_time):
    timestamp = str(time.mktime(datetime_time.timetuple()))[:-2]
    return datetime.utcfromtimestamp(int(timestamp))
