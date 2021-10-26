import pandas as pd


def write_pipelines_to_csv(pipelines):
    df = pd.DataFrame(pipelines)
    print(df)
    df.to_csv("./test.csv", sep=",", encoding="utf-8", header=True)
