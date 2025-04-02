from statistic import GraphicStatistics
def main():
    df_path = 'states.csv'
    stats = GraphicStatistics(df_path)
    stats.histogram()


if __name__ == '__main__':
    main()