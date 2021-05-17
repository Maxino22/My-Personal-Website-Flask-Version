import os
from PIL import Image
from flask import url_for, current_app


def add_profile_pic(pic_upload, first_name):
    filename = pic_upload.filename

    ext_type = filename.split('.')[-1]
    storage_filename = str(first_name) + '.' + ext_type

    filepath = os.path.join(current_app.root_path,
                            'static/profile_pics', storage_filename)

    output_size = (960, 960)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename

def add_port_pic(pic_upload, first_name):
    filename = pic_upload.filename

    ext_type = filename.split('.')[-1]
    storage_filename = str(first_name) + '.' + ext_type

    filepath = os.path.join(current_app.root_path,
                            'static/port_pics', storage_filename)

    output_size = (250, 250)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename


