import tushare as ts


def main():
    # print("获取股票历史数据")
    # print( ts.get_hist_data('601688') )

    # print("股票实时行情")
    # print(ts.get_realtime_quotes('000002'))

    # print("存款利率")
    # print( ts.get_deposit_rate())

    # print("电影票")
    # print(ts.realtime_boxoffice())
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt

    df = ts.get_hist_data('sz50', start='2016-11-01', end='2016-12-30')
    #df.to_excel('stock_sh.xlsx')
    df.close.plot()
    ax = plt.gca()
    ax.invert_xaxis()
    plt.show()

if __name__ == '__main__':
    main()