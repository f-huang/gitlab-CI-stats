import argparse
from gitlab_api import print_token, get_project_by_id, get_project_pipelines


if __name__ == '__main__':
  print("Hello World !")

  parser = argparse.ArgumentParser()
  parser.add_argument("project_id", type=int, help="GitLab's project id")
  args = parser.parse_args()

  print_token()
  project = get_project_by_id(args.project_id)
  print(project)
  pipelines = get_project_pipelines(args.project_id)
  print(pipelines)