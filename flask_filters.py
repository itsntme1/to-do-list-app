from datetime import datetime

def formatNone(val):
    if not val or str == None:
        return ''
    
    return val

def format_date(date):
    return datetime.fromisoformat(date).strftime('%Y-%m-%d')

def priorityTextBgColor(priority):
    if priority == 3:
        return 'text-bg-danger'
    elif priority == 2:
        return 'text-white bg-warning'
    elif priority == 1:
        return 'text-bg-success'
    else:
        return ''
    
def priorityTableColor(priority):
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
        return 'Hard'
    elif priority == 2:
        return 'Medium'
    elif priority == 1:
        return 'Easy'
    else:
        return priority