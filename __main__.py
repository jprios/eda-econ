# __main__.py
from eda_report import load_data, treat_data, load_continent_data, merge_datasets, select_year, cat_box_plot, cat_scatter_plot

def main():
    # Carregar e tratar dados
    df = load_data()
    df = treat_data(df)
    continents = load_continent_data()
    df_final = merge_datasets(df, continents)

    # Exemplo de uso de gráficos
    df_2020 = select_year(df_final, 2020)
    cat_box_plot(df_2020, y_var='gdp_growth', cat='continent', color_cat='continent')
    cat_scatter_plot(df_2020, x_var='real_interest_rate', y_var='inflation', color_cat='continent')

if __name__ == '__main__':
    main()
