# ============================================================
# ДЗ 1: Даты — get_days_from_today
# ============================================================

from datetime import datetime  

date = "2020-10-09"  

def get_days_from_today(date): 
    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d")  
    except ValueError:
        return  
    current_date = datetime.today()  
    days_count = current_date.toordinal() - formatted_date.toordinal()  
    return days_count  


# ============================================================
# ДЗ 2: Лотерея — get_numbers_ticket
# ============================================================

import random  # импорт генератора случайных чисел

def get_numbers_ticket(min, max, quantity):  
    if min < 1:  
        return []
    if max > 1000:  
        return []
    if min >= max:  
        return []
    if quantity < 1:  
        return []
    if quantity > (max - min + 1):  
        return []
    numbers = set()  
    while len(numbers) < quantity:  
        num = random.randint(min, max)  
        numbers.add(num)  
    lottery_numbers = list(numbers)  
    lottery_numbers.sort()  
    return lottery_numbers  


# ============================================================
# ДЗ 3: Номера — normalize_phone
# ============================================================

import re  

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]  

def normalize_phone(phone_number):  
    pattern = r"[^\d\+]"  
    replacement = "" 
    clean = re.sub(pattern, replacement, phone_number)  
    if clean.startswith("+380"): 
        return clean
    if clean.startswith("380"):  
        return "+" + clean
    if clean.startswith("0"): 
        return "+38" + clean
    else:
        return clean 