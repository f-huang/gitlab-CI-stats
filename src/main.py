import argparse
from gitlab_pipelines import get_pipelines_by_date, hydrate_pipelines
from csv_writer import write_pipelines_to_csv

if __name__ == '__main__':
    print("Hello World !")

    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", type=int, help="GitLab's project id")
    args = parser.parse_args()

    pipelines = get_pipelines_by_date(args.project_id, "2021-01-01")
    pipelines = hydrate_pipelines(args.project_id, pipelines)

    write_pipelines_to_csv(pipelines)
