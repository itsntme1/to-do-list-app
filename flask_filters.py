from datetime import datetime

def isEmpty(val):
    if not val or str == None:
        return True
    
    return False

def format_date(date):
    return datetime.fromisoformat(date).strftime('%Y-%m-%d')