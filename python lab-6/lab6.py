from datetime import datetime

def logger(file=None, log_type=None):
    log = []
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            call_info = {
                "timestamp": datetime.now(),
                "function_name": func.__name__,
                "args": args,
                "kwargs": kwargs,
                "result": result,
                "log_type": log_type
            }
            log.append(call_info)
            if file:
                with open(file, 'a') as log_file:
                    log_file.write(f"Тип: {call_info['log_type']}, Функція: {call_info['function_name']}, Аргументи: {call_info['args']}, Результат: {call_info['result']}, Час виклику: {call_info['timestamp']}\n")
            return result
        wrapper.log = log
        return wrapper
    return decorator


def get_logs():
    for log_entry in wrapper.log:  
        yield log_entry


@logger(file="log.txt", log_type="info")
def add(a, b):
    return a + b

@logger(file="log.txt", log_type="info")
def subtract(a, b):
    return a - b

@logger(file="log.txt", log_type="error")
def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ділення на нуль неможливе!")
        return None


add(3, 4)
subtract(10, 5)
divide(7, 0)


log = get_logs()
print("Історія викликів:")
for entry in log:
    print(f"Тип: {entry['log_type']}, Функція: {entry['function_name']}, Аргументи: {entry['args']}, Результат: {entry['result']}, Час виклику: {entry['timestamp']}")
