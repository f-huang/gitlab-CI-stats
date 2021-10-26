import pandas as pd


def write_pipelines_to_csv(output_filepath: str, pipelines):
    df = pd.DataFrame(pipelines)
    print(df)
    df.to_csv(output_filepath, sep=",", encoding="utf-8", header=True)
