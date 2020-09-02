from datetime import datetime, date

import pytz


# Convert string value ('True'/'False') to boolean value
def str_to_bool(strbool):
    if strbool.lower() == 'true':
        return True
    elif strbool.lower() == 'false':
        return False
    else:
        raise ValueError


# Validates/Convert text date (Year-Month-day) in DateTime object (timezone SP/Brazil)
def validate_date(date_text):
    timezone = pytz.timezone('America/Sao_Paulo')
    try:
        dt = timezone.localize(datetime.strptime(date_text + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))
        return dt
    except ValueError:
        dt = timezone.localize(datetime.today())
        return dt


# Convert timestamp value to string (Year-Month-Day)
def timestamp_to_formated_date(dt):
    return datetime.fromtimestamp(int(dt)/1000).strftime('%Y-%m-%d')


# Convert 'MongoDB Document' in 'News' object
def adjust_news(news):
    return {
        'id': news['_id']['$oid'],
        'title': news['title'],
        'content': news['content'],
        'publish_date': timestamp_to_formated_date(news['publish_date']['$date'])}


# Convert list of 'MongoDB Document' in lista of 'News' object
def adjust_dict_news(list_bson):
    list_news = []

    for item in list_bson:
        elem = adjust_news(item)
        list_news.append(elem)

    return list_news


def create_now():
    timezone = pytz.timezone('America/Sao_Paulo')
    today_tz = datetime.now(tz=timezone)
    return today_tz
