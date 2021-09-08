
def count_missing_ratio(df, vis=True):
    """
    Count the missing rate of each column
    :param df: pandas.DataFrame, the source of data
    :param vis: look the result
    :return: missing_res: dict, every column's missing rate
    """
    missing_res = {}
    for col in df.columns:
        res = df[col].isnull().sum()
        ratio = round(res / df.shape[0], 4)
        missing_res[col] = ratio
        if vis:
            print("{}: {:.2f}%".format(col, ratio * 100))
    return missing_res


def filter_missing_col(df, thr, vis=True):
    """
    Filter out columns with a missing rate greater than thr.
    :param df: pandas.DataFrame, the source of data
    :param thr: float, the thresholds, 0.0～1.0
    :param vis: look the result
    :return: filter_col:list, the name of filtered columns
    """
    filter_col = []
    for col in df.columns:
        res = df[col].isnull().sum()
        ratio = round(res / df.shape[0], 4)
        if ratio <= thr:
            filter_col.append(col)
            if vis:
                print("{}: {:.2f}%".format(col, ratio*100))
    return filter_col