import threading
import time
from traceback import format_exc
from typing import Callable, TYPE_CHECKING
from math import sin, cos
import hashlib, os
import re

from shapely.affinity import rotate

from .logger import error

if TYPE_CHECKING:
    from shapely import geometry


def rotated_rect(cx: float, cy: float, w: float, h: float, facing_rad: float) -> 'geometry.Polygon':
    from shapely import geometry
    return rotate(geometry.box(cx - w / 2, cy, cx + w / 2, cy + h), -facing_rad, origin=(cx, cy), use_radians=True)


def circle(cx: float, cy: float, radius: float) -> 'geometry.Polygon':
    from shapely import geometry
    return geometry.Point(cx, cy).buffer(radius)


def sector(cx: float, cy: float, radius: float, angle_rad: float, facing_rad: float, steps: int = 100) -> 'geometry.Polygon':
    from shapely import geometry
    step_angle_width = angle_rad / steps
    segment_vertices = [(cx, cy), (cx, cy + radius)]
    segment_vertices += [(cx + sin(i * step_angle_width) * radius, cy + cos(i * step_angle_width) * radius) for i in range(1, steps)]
    return rotate(geometry.Polygon(segment_vertices), -(facing_rad - angle_rad / 2), origin=(cx, cy), use_radians=True)


def query(iterator, key: Callable[[any], bool], limit: int = None):
    count = 0
    for item in iterator:
        if key(item):
            count += 1
            yield item
            if limit is not None and limit <= count:
                return


def dir_hash(directory_path):
    hashs = hashlib.sha256()
    if not os.path.exists(directory_path):
        return None
    for root, dirs, files in os.walk(directory_path):
        for names in files:
            filepath = os.path.join(root, names)
            with open(filepath, 'rb') as f1:
                while True:
                    buf = f1.read(4096)
                    if not buf: break
                    hashs.update(hashlib.sha256(buf).digest())
    return hashs.hexdigest()


def file_hash(file_path):
    if not os.path.exists(file_path):
        return None
    hashs = hashlib.sha256()
    with open(file_path, 'rb') as f1:
        while True:
            buf = f1.read(4096)
            if not buf: break
            hashs.update(hashlib.sha256(buf).digest())
    return hashs.hexdigest()


def get_hash(path):
    if os.path.isdir(path):
        return dir_hash(path)
    else:
        return file_hash(path)


class Counter(object):
    def __init__(self):
        self.current = 0
        self._lock = threading.Lock()

    def get(self):
        with self._lock:
            self.current += 1
            return self.current

    def reset(self):
        with self._lock:
            self.current = 0


class WaitTimeoutException(Exception):
    def __init__(self):
        super(WaitTimeoutException, self).__init__("Wait Timeout")


def wait_until(statement: Callable[[], any], timeout: float = None, period: float = 0.1):
    temp = statement()
    start = time.perf_counter()
    while temp is None:
        if timeout is not None and time.perf_counter() - start >= timeout:
            raise WaitTimeoutException()
        time.sleep(period)
        temp = statement()
    return temp


def err_catch(func):
    def warper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            error('error_catch', format_exc())

    return warper


utf8_remove = re.compile(r'(\a|\b|\f|\n|\r|\t|\v|[\x01-\x1F])')


def utf8_clean_up(string_bytes: bytes):
    return utf8_remove.sub("", string_bytes.decode('utf-8', errors='ignore'))


class TimeoutException(Exception): pass


