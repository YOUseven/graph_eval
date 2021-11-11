import pandas as pd

def count_black_ratio(df, shouxin_m='shouxin_m', product_no='product_no', y_col='dpd30_n6', y=0):
    """
    输出样本统计的黑白样本率
    :param df:
    :param shouxin_m:
    :param product_no:
    :param y:
    :return:
    """
    print("------------------整体样本------------------")
    print("黑白样本数\t黑样本\t黑样本率：{}\t{}\t{:.2f}%".format(df.shape[0],
                                                            df[y_col].value_counts()[y],
                                                            df[y_col].value_counts()[y] * 100. / df.shape[0]))

    print("------------------分月样本------------------")
    print("月份\t黑白样本数\t黑样本\t黑样本率")
    print(df.groupby(shouxin_m).apply(
        lambda df: "{} {}  {:.2f}%".format(df.shape[0], df[y_col].value_counts()[y],
                                           df[y_col].value_counts()[y] * 100. / df.shape[0])))

    print("------------------分产品样本------------------")
    print("产品\t黑白样本数\t黑样本\t黑样本率")
    print(df.groupby(product_no).apply(
        lambda df: "{} {}  {:.2f}%".format(df.shape[0], df[y_col].value_counts()[y],
                                           df[y_col].value_counts()[y] * 100. / df.shape[0])))

    print("------------------分产品分月样本------------------")
    print("产品\t黑白样本数\t黑样本\t黑样本率")
    print(df.groupby([product_no,shouxin_m]).apply(
        lambda df: "{} {}  {:.2f}%".format(df.shape[0], df[y_col].value_counts()[y],
                                           df[y_col].value_counts()[y] * 100. / df.shape[0])))

    print("------------------分月分产品样本------------------")
    print("产品\t黑白样本数\t黑样本\t黑样本率")
    print(df.groupby([product_no, shouxin_m]).apply(
        lambda df: "{} {}  {:.2f}%".format(df.shape[0], df[y_col].value_counts()[y],
                                           df[y_col].value_counts()[y] * 100. / df.shape[0])))
