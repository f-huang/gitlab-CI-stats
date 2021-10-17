import os
from dotenv import load_dotenv
load_dotenv()

GITLAB_ACCESS_TOKEN = os.environ.get("GITLAB_ACCESS_TOKEN")

def print_token(): 
  print("GITLAB_ACCESS_TOKEN", GITLAB_ACCESS_TOKEN)
