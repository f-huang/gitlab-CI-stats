import argparse
from gitlab_api import get_project_pipelines


if __name__ == '__main__':
    print("Hello World !")

    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", type=int, help="GitLab's project id")
    args = parser.parse_args()

    pipelines = get_project_pipelines(args.project_id)
    print(pipelines)
