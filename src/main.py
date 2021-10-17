from gitlab_api import print_token, get_project_by_id

if __name__ == '__main__':
  print("Hello World !")
  print_token()
  project = get_project_by_id(11060619)
  print(project)