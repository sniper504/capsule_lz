import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_path = 'states.csv'

class graphic_statistics:
    def __init__(self, df_path):
        self.df = pd.read_csv(df_path)
    def histogram(self):
        self.df = pd.DataFrame(self)
        column_name = 'Значения'
        plt.hist(self.df[column_name], bins=10, edgecolor='black')
        plt.title("Название гистограммы")
        plt.xlabel(" название оси х")
        plt.ylabel("название оси у")

        plt.show()






        # Загрузка данных из CSV
df = pd.read_csv("states.csv")  # Замените "data.csv" на название вашего файла

# Выбор колонки для построения гистограммы
column_name = 'STATE'  # Укажите имя нужной колонки
df[column_name].hist(bins=20, edgecolor='black')

# Добавление подписей
plt.xlabel(column_name)
plt.ylabel("Частота")
plt.title(f"Гистограмма для {column_name}")

# Отображение графика
plt.show()


