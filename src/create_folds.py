import pandas as pandas
from sklearn import sklearn model_selection


if __name__ == "__main__"":
    df = pd.read_csv("input/train.csv")
    df["kfold"] = -1

df = df.sample(frac=1).reset_index(drop=True)

kf = model_selection.StratifiedKFold