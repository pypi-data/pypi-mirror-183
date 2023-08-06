from collections import defaultdict
from functools import wraps
from unittest import mock


def read_decorator(
    f_py=None,
):
    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with mock.patch("os.path.isfile") as mock_isfile:
                mock_isfile.return_value = True
                with mock.patch("os.path.exists") as mock_path_ex:
                    mock_path_ex.return_value = True
                    try:
                        p = mock.patch(
                            "builtins.open",
                            mock.mock_open(read_data=kwargs["_file_data"]),
                        )
                        p.start()
                        babax = func(*args, **kwargs)
                    finally:
                        try:
                            p.stop()
                        except Exception:
                            pass

            return babax

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator


def write_decorator(
    f_py=None,
):
    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with mock.patch("os.path.isfile") as mock_isfile:
                mock_isfile.return_value = False

                with mock.patch("os.path.exists") as mock_path_ex:
                    mock_path_ex.return_value = False

                    try:
                        p = mock.patch("builtins.open", mock.mock_open())
                        p.start()
                        babax = func(*args, **kwargs)
                        allresa = []

                        for ini, _ in enumerate(open.mock_calls):
                            name, args, kwargs = _
                            allresa.append((ini, name, args, kwargs))
                        fi = defaultdict(list)
                        rightnow = ""
                        for x in allresa:
                            if (x[1]) == "":
                                rightnow = x[2]
                            elif (x[1]) == "().write":
                                fi[rightnow].append(x[2][0])
                            else:
                                continue

                        fi2 = {}
                        for key, item in fi.items():
                            if any(item):
                                if isinstance(item[0], bytes):
                                    fi2[key[0]] = b"".join(item)
                                else:
                                    fi2[key[0]] = "".join(item)

                        babax = fi2.copy()
                    finally:
                        try:
                            p.stop()
                        except Exception:
                            pass
            return babax

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
