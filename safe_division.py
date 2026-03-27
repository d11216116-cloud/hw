def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "錯誤：除數不能為零！"
