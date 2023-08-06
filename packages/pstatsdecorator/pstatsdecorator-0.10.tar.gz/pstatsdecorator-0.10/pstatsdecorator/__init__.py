import cProfile
import io
import pstats
from functools import wraps


def pstats_check(f_py=None, print_stats=True, return_stats=True, sortby="filename"):
    r"""
    sortby:
    'calls'
    'cumulative'
    'cumtime'
    'file'
    'filename'
    'module'
    'ncalls'
    'pcalls'
    'line'
    'name'
    'nfl'
    'stdname'
    'time'
    'tottime'
    """
    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            vala = None
            try:
                prof = cProfile.Profile()
                prof.enable()
                vala = prof.runcall(func, *args, **kwargs)
            finally:
                try:
                    prof.disable()
                except Exception:
                    pass
            s = io.StringIO()
            ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
            ps.print_stats()
            rea = s.getvalue()
            if print_stats:
                print(rea)
            if return_stats:
                return vala, rea
            else:
                return vala

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
