import random, time_uuid
from datetime import datetime,timedelta, timezone

def currentTime7():
    now = datetime.now()
    d = datetime.fromisoformat(now.isoformat())
    tz = timezone(timedelta(hours=7))
    return d.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

def generate_uuids_byTime7():
    now = datetime.now()
    d = datetime.fromisoformat(now.isoformat())
    tz = timezone(timedelta(hours=7))

    rand_time = lambda: float(random.randrange(0,100)) + d.astimezone(tz).timestamp()#time_uuid.utctime()
    uuids_tz7 = time_uuid.TimeUUID.with_timestamp(rand_time()) 
    return uuids_tz7

def convert_timestamp_to_datetimezone7(_timestamp):
    dt = datetime.fromtimestamp(_timestamp / 1e3)
    dtiso = datetime.fromisoformat(dt.isoformat())
    tz = timezone(timedelta(hours=7))
    return dtiso.astimezone(tz).strftime('%Y-%m-%dT%H:%M:%S.%f%z')

def difference_datetimezone7_by_day_from_now(_dtz_target):
    tz = timezone(timedelta(hours=7))
    dtz_now = datetime.fromisoformat(datetime.now().isoformat()).astimezone(tz)
    dtz_target = datetime.strptime(str(_dtz_target).strip(),'%Y-%m-%dT%H:%M:%S.%f%z')
    return (dtz_now-dtz_target).days