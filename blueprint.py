import os
import shutil

from flask import Blueprint
from tarbell.hooks import register_hook
from clint.textui import puts, colored # Comes with Tarbell

NAME = "RG Form Chart Blueprint"
blueprint = Blueprint("base", __name__)

@register_hook('newproject')
def newproject_copy(site):
    """ Copy _includes and raw directories to new project """
    blueprint_path = os.path.join(site.path, '_blueprint')
    
    puts("Copying _includes to new project")
    shutil.copy(os.path.join(blueprint_path, '_includes'), os.path.join(site.path, '_includes'))
    
    puts("Copying raw to new project")
    shutil.copy(os.path.join(blueprint_path, 'raw'), os.path.join(site.path, 'raw'))

@blueprint.app_template_filter()
def process_text(text, scrub=True):
    """
    Converts "<" to "&lt;" to display HTML
    Stolen from https://github.com/eads/tarbell-grunt-template/
    """
    try:
        return Markup(text)
    except TypeError:
        return ""

@blueprint.app_template_filter()
def format_date(value, format='%b. %d, %Y', convert_tz=None):
    """
    Format a date.
    Stolen from https://github.com/eads/tarbell-grunt-template/
    """
    if isinstance(value, float) or isinstance(value, int):
        seconds = (value - 25569) * 86400.0
        parsed = datetime.datetime.utcfromtimestamp(seconds)
    else:
        parsed = dateutil.parser.parse(value)
    if convert_tz:
        local_zone = dateutil.tz.gettz(convert_tz)
        parsed = parsed.astimezone(tz=local_zone)

    return parsed.strftime(format)