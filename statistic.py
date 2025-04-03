import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class GraphicStatistics:
    def __init__(self, df_path):
        self.df = pd.read_csv(df_path)

    def histogram(self):
        # Группируем данные по штатам и вычисляем среднее
        grouped_df = self.df.groupby("STATE", as_index=False).mean()

        states = grouped_df["STATE"]
        federal_avg = grouped_df["FEDERAL_REVENUE"]
        state_avg = grouped_df["STATE_REVENUE"]
        local_avg = grouped_df["LOCAL_REVENUE"]

        x = np.arange(len(states)) * 2  # Увеличиваем расстояние между столбцами

        # Рассчитываем процентное соотношение
        total_budget = federal_avg + state_avg + local_avg
        federal_percent = (federal_avg / total_budget) * 100
        state_budget_percent = (state_avg / total_budget) * 100
        local_budget_percent = (local_avg / total_budget) * 100

        # Создаем график
        fig, ax = plt.subplots(figsize=(25, 15))  # Увеличенный размер графика
        bar_width = 1.5  # Ширина столбцов

        # График отображает проценты
        ax.bar(x, federal_percent, color="blue", width=bar_width, label="Федеральный бюджет")
        ax.bar(x, state_budget_percent, bottom=federal_percent, color="green", width=bar_width, label="Бюджет штата")
        ax.bar(x, local_budget_percent, bottom=federal_percent + state_budget_percent, color="orange", width=bar_width, label="Местный бюджет")

        # Выводим средние значения внутри столбцов
        for i in range(len(states)):
            ax.text(x[i], federal_percent.iloc[i] / 2, f"{federal_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=3)
            ax.text(x[i], federal_percent.iloc[i] + state_budget_percent.iloc[i] / 2, f"{state_budget_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=3)
            ax.text(x[i], federal_percent.iloc[i] + state_budget_percent.iloc[i] + local_budget_percent.iloc[i] / 2, f"{local_budget_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=3)

        # Координаты для текста слева
        left_x = -5  # Смещаем левый текст за пределы графика
        left_y_federal = -3
        left_y_state = -4
        left_y_local = -4.5

        # Добавляем подписи слева
        ax.text(left_x, left_y_federal, "Федеральный бюджет", ha="right", fontsize=4)
        ax.text(left_x, left_y_state, "Бюджет штата", ha="right", fontsize=4)
        ax.text(left_x, left_y_local, "Местный бюджет", ha="right", fontsize=4)

        # Выводим значения под столбцами, уменьшаем шрифт для читаемости
        for i in range(len(states)):
            ax.text(x[i], -3, f"{federal_avg.iloc[i]:.1f}", ha="center", fontsize=2)
            ax.text(x[i], -4, f"{state_avg.iloc[i]:.1f}", ha="center", fontsize=2)
            ax.text(x[i], -4.5, f"{local_avg.iloc[i]:.1f}", ha="center", fontsize=2)

        # Настройки осей
        ax.set_xticks(x)
        ax.set_xticklabels(states, rotation=0, ha="right", fontsize=2)  # Лёгкий наклон для читаемости
        ax.set_ylim(0, 110)
        plt.subplots_adjust(bottom=0.1)  # Поднимаем график, увеличивая место снизу


        ax.set_ylabel("%")
        ax.set_title("Средние бюджеты школ по всем штатам (в %)")

        # Перемещение легенды под график в одну строку
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=3, frameon=False, fontsize = 3)

        plt.tight_layout()
        plt.show()

# Использование
df_path = 'states.csv'
stats = GraphicStatistics(df_path)
stats.histogram()







