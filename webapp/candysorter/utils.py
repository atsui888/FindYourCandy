# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

import errno
import importlib
import os
import random
import string


def load_class(name):
    parts = name.split('.')
    module = importlib.import_module('.'.join(parts[:-1]))
    return getattr(module, parts[-1])


def symlink_force(source, link_name):
    try:
        os.symlink(source, link_name)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.unlink(link_name)
            os.symlink(source, link_name)
        else:
            raise e


def random_str(length, chars=string.ascii_letters + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])
