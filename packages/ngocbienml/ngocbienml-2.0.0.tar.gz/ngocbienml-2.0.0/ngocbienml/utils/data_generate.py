import numpy as np
import pandas as pd


def __gen_columns_name__(columns_num, candidate=None):
    assert columns_num < 26 ** 2
    all_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    columns = []
    if columns_num <= len(all_char):
        columns = list(all_char[:columns_num])
    else:
        count = 0
        for i in all_char:
            for j in all_char:
                columns.append(i + j)
                count += 1
                if count >= columns_num:
                    break
            if count >= columns_num:
                break
    print(len(columns))
    assert len(columns) == columns_num
    return columns


def __gen_dtypes__(ncols, dtypes=None):
    if dtypes is not None:
        assert len(dtypes) == ncols
    else:
        dtypes = (np.random.randint if np.random.uniform() > .5 else np.random.normal)
    assert set(dtypes) <= set(('int', 'float', 'cat'))


def numeric_pandas(nrows=1000, ncols=5):
    columns = __gen_columns_name__(columns_num=ncols)
    df = pd.DataFrame()


def get_fast_pandas(nrows=10_000):
    df = pd.DataFrame()
    df['A'] = np.random.randint(0, 10, size=(nrows,))
    df['B'] = np.random.randint(0, 100, size=(nrows,))
    df['C'] = np.random.uniform(size=(nrows,))
    df['D'] = np.random.normal(0, 1, size=(nrows,))
    df['E'] = np.random.randint(0, 2, size=(nrows,))

    df['label'] = np.random.randint(0, 2, size=(nrows,))
    return df


def get_fast_complex_pandas(nrows=10_000):
    df = get_fast_pandas(nrows)
    df['CAT1'] = np.random.choice(np.asarray(list('AB')).reshape(-1, ), size=(nrows,))
    df['CAT2'] = np.random.choice(np.asarray(list('ABCD')).reshape(-1, ), size=(nrows,))
    df['CAT3'] = np.random.choice(np.asarray(list('ABCDEFGHIJ')).reshape(-1, ), size=(nrows,))
    df['CAT4'] = np.random.choice(np.asarray(list('ABCDEFGHIJKLMH')).reshape(-1, ), size=(nrows,))
    return df


if __name__ == "__main__":
    pass


