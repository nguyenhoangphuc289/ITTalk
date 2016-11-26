from django import template

register = template.Library()


@register.inclusion_tag("home/feed.html")
def show_feed():
    topics = [
        'Python',
        'Django',
        'ASP.NET',
        'Drupal',
        'Window Form',
    ]
    return {'topics': topics}


@register.inclusion_tag("home/event.html")
def show_event():
    events = [
        'Seminar Django', 'Seminar Android', 'Talk about SQLite'
    ]
    return {'events': events}

@register.simple_tag
def get_user_id():
    return