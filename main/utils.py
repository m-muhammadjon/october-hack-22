import os

from django.utils import timezone, dateformat


def generate_upload_path(instance, filename):
    app_label = instance._meta.app_label
    model_name = instance._meta.model_name
    now = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    *file, exc = split_file_name(filename)
    file = '.'.join(file)
    if hasattr(instance, 'category'):
        filepath = "%s/%s/%s/%s-%s.%s" % (
            app_label, model_name, instance.category, file, now, exc
        )
    else:
        filepath = "%s/%s/%s-%s.%s" % (
            app_label, model_name, file, now, exc
        )
    return filepath


def split_file_name(filename):
    """path/file.exe => file, exe"""
    filename = filename.split(os.sep)[-1]
    return filename.split('.')


