def datetime_in_ms():
    from datetime import datetime
    date_str = datetime.now()
    datefrom = datetime.strptime(str(date_str),"%Y-%m-%d %H:%M:%S.%f").strftime('%s.%f')
    date_in_ms = int(float(datefrom)*1000)
    return date_in_ms