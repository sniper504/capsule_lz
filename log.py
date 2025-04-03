import os
import pandas as pd
from datetime import date, datetime

def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)

        username = os.getlogin()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.now().strftime("%H:%M:%S")
        file_path = "logs.csv"

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            file_df = pd.read_csv(file_path)

            # Вычисляем новый id
            new_id = file_df.shape[0]

            # Создаём новую строку
            new_row = pd.DataFrame({
                'id': [new_id],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })

            # Записываем строку в `logs.csv`
            new_row.to_csv(file_path, mode='a', header=False, index=False)
        
        else:
            # Создаём файл с заголовками
            df = pd.DataFrame({
                'id': [0],
                'pc_username': [username],
                'function_name': [func_name],
                'Date in date.month.year': [formatted_date],
                'Time': [formatted_time]
            })

            df.to_csv(file_path, index=False)

        print(f" Данные успешно записаны в {file_path}")
        return original_result

    return wrapper

