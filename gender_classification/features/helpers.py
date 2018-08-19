# -*- coding: utf-8 -*-


def cast_response_to_int(func):
    """If a function returns boolean or None,
        casts it to an integer:
        True -> 1
        False -> 0
        None -> 0

       Moreover, it wraps function call with a try/catch block
       and returns 0, if an Exception. Exceptions might happen because
       of some missing keys in the event.
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(e)
            return 0
        if type(result) == bool:
            result = int(result)
        elif result is None:
            result = 0
        return result

    return wrapper
