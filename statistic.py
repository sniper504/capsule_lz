import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class GraphicStatistics:
    def __init__(self, df_path):
        self.df = pd.read_csv(df_path)

    def histogram(self):
        # Группируем данные по штатам и вычисляем среднее
        grouped_df = self.df.groupby("STATE", as_index=False).mean()

        # Выбираем нужные штаты
        selected_states = ["Texas", "California", "Alabama", "Utah", "Washington", "Hawaii"]
        filtered_df = grouped_df[grouped_df["STATE"].isin(selected_states)]

        states = filtered_df["STATE"]
        federal_avg = filtered_df["FEDERAL_REVENUE"]
        state_avg = filtered_df["STATE_REVENUE"]
        local_avg = filtered_df["LOCAL_REVENUE"]


        x = np.arange(len(states))

        # Вычисляем пропорции внутри каждого столбца, чтобы сделать их одинаковой высоты
        fixed_height = 80 # Фиксированная высота столбцов
        total_budget = federal_avg + state_avg + local_avg

        federal_percent = (federal_avg / total_budget) * 100  # В процентах
        state_budget_percent = (state_avg / total_budget) * 100
        local_budget_percent = (local_avg / total_budget) * 100

        # Создаем график
        fig, ax = plt.subplots(figsize=(10, 6))
        bar_width = 0.8

        # График  отображает проценты
        ax.bar(x, federal_percent, color="blue", width=bar_width, label="Федеральный бюджет")
        ax.bar(x, state_budget_percent, bottom=federal_percent, color="green", width=bar_width, label="Бюджет штата")
        ax.bar(x, local_budget_percent, bottom=federal_percent + state_budget_percent, color="orange", width=bar_width, label="Местный бюджет")
        # Выводим средние значения на графике
        for i in range(len(states)):
            ax.text(x[i], federal_percent.iloc[i] / 2, f"{federal_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=10)
            ax.text(x[i], federal_percent.iloc[i] + state_budget_percent.iloc[i] / 2, f"{state_budget_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=10)
            ax.text(x[i], federal_percent.iloc[i] + state_budget_percent.iloc[i] + local_budget_percent.iloc[i] / 2, f"{local_budget_percent.iloc[i]:.1f}%", ha="center", color="white", fontsize=10)


        # Координаты для текста слева
        left_x = -1.5  # Смещаем левый текст за пределы графика
        left_y_federal = -20
        left_y_state = -40
        left_y_local = -60

        # Добавляем подписи слева
        ax.text(left_x, left_y_federal, "Федеральный бюджет", ha="right", fontsize=12)
        ax.text(left_x, left_y_state, "Бюджет штата", ha="right", fontsize=12)
        ax.text(left_x, left_y_local, "Местный бюджет", ha="right", fontsize=12)

        # Выводим значения под столбцами
        for i in range(len(states)):
            ax.text(x[i], left_y_federal, f"{federal_avg.iloc[i]:.1f}", ha="center", fontsize=12)
            ax.text(x[i], left_y_state, f"{state_avg.iloc[i]:.1f}", ha="center", fontsize=12)
            ax.text(x[i], left_y_local, f"{local_avg.iloc[i]:.1f}", ha="center", fontsize=12)


        # Настройки осей
        ax.set_xticks(x)
        ax.set_xticklabels(states, rotation=0, ha="center", fontsize=12)
        ax.set_ylim(0,110)
        plt.tight_layout(pad=3)  # Добавляем немного отступа


        ax.set_ylabel("%")
        ax.set_title("Средние бюджеты школ по выбранным штатам")
        ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.6), ncol=3, frameon=False)


        plt.tight_layout()
        plt.show()

# Использование
df_path = 'states.csv'
stats = GraphicStatistics(df_path)
stats.histogram()


