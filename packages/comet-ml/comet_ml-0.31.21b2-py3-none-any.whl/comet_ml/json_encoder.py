# -*- coding: utf-8 -*-
# *******************************************************
#   ____                     _               _
#  / ___|___  _ __ ___   ___| |_   _ __ ___ | |
# | |   / _ \| '_ ` _ \ / _ \ __| | '_ ` _ \| |
# | |__| (_) | | | | | |  __/ |_ _| | | | | | |
#  \____\___/|_| |_| |_|\___|\__(_)_| |_| |_|_|
#
#  Sign up for free at https://www.comet.com
#  Copyright (C) 2015-2021 Comet ML INC
#  This file can not be copied and/or distributed without the express
#  permission of Comet ML Inc.
# *******************************************************
import traceback
from inspect import istraceback
from typing import IO, Any, Union

import simplejson

convert_functions = []

try:
    import numpy

    def convert_numpy_array_pre_1_16(value):
        try:
            return numpy.asscalar(value)
        except (ValueError, IndexError, AttributeError, TypeError):
            return None

    def convert_numpy_array_post_1_16(value):
        try:
            return value.item()
        except (ValueError, IndexError, AttributeError, TypeError):
            return None

    convert_functions.append(convert_numpy_array_post_1_16)
    convert_functions.append(convert_numpy_array_pre_1_16)
except ImportError:
    pass


def _set_comet_defaults(**kwargs: Any):
    """
    Set default values to be used by JSON encoder with Comet data packages.
    """
    if "default" not in kwargs:
        kwargs["default"] = comet_serializer
    if "ignore_nan" not in kwargs:
        kwargs["ignore_nan"] = True

    return kwargs


def dumps(obj: Any, *args: Any, **kwargs: Any) -> str:
    """
    The wrapper allowing us to change underlying implementation
    """
    kwargs = _set_comet_defaults(**kwargs)
    return simplejson.dumps(obj, *args, **kwargs)


def dump(obj: Any, fp: IO[str], *args: Any, **kwargs: Any) -> None:
    """
    The wrapper allowing us to change underlying implementation
    """
    kwargs = _set_comet_defaults(**kwargs)
    simplejson.dump(obj, fp, *args, **kwargs)


def loads(s: Union[str, bytes, bytearray], **kwargs: Any) -> Any:
    """
    The wrapper allowing us to change underlying implementation
    """
    return simplejson.loads(s, **kwargs)


def load(fp: IO[str], **kwargs: Any):
    """
    The wrapper allowing us to change underlying implementation
    """
    return simplejson.load(fp, **kwargs)


def comet_serializer(obj):

    # Custom conversion
    if type(obj) == Exception or isinstance(obj, Exception) or type(obj) == type:
        return str(obj)

    elif istraceback(obj):
        return "".join(traceback.format_tb(obj)).strip()

    elif hasattr(obj, "repr_json"):
        return obj.repr_json()

    elif isinstance(obj, complex):
        return str(obj)

    # try to convert Numpy scalar types
    converted_obj = convert(obj)
    if converted_obj is not None:
        return converted_obj

    # everything failed
    raise TypeError("%s is not JSON serializable" % obj.__class__.__name__)


def convert(obj):
    """
    Try converting the obj to something json-encodable
    """
    for converter in convert_functions:
        converted = converter(obj)

        if converted is not None:
            return converted

    return None
