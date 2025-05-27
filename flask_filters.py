from datetime import datetime

def format_none(val):
    if not val or str == None:
        return ''
    
    return val

def format_date(date):
    return datetime.fromisoformat(date).strftime('%Y-%m-%d')

def priority_text_bg_color(priority):
    if priority == 3:
        return 'text-bg-danger'
    elif priority == 2:
        return 'text-white bg-warning'
    elif priority == 1:
        return 'text-bg-success'
    else:
        return ''
    
def priority_table_color(priority):
    if priority == 3:
        return 'table-danger'
    elif priority == 2:
        return 'table-warning'
    elif priority == 1:
        return 'table-success'
    else:
        return ''
    
def format_priority(priority):
    if priority == 3:
        return 'Critical'
    elif priority == 2:
        return 'Necessary'
    elif priority == 1:
        return 'Optional'
    else:
        return priority
    
def format_status_table(status):
    if status == 'completed':
        return 'table-success'
    elif status == 'canceled':
        return 'table-danger'
    elif status == 'pending':
        return 'table-warning'
    else:
        return ''