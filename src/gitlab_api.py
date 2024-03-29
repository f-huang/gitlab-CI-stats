import os
import requests

from dotenv import load_dotenv
load_dotenv()

GITLAB_ACCESS_TOKEN = os.environ.get("GITLAB_ACCESS_TOKEN")
GITLAB_API_VERSION = "v4"
GITLAB_REST_ENDPOINT = "https://gitlab.com/api/{version}".format(
    version=GITLAB_API_VERSION)
GITLAB_REQUEST_HEADERS = {'Authorization': 'Bearer ' +
                          GITLAB_ACCESS_TOKEN, 'Content-Type': 'multipart/form-data'}


def print_token():
    print("GITLAB_ACCESS_TOKEN", GITLAB_ACCESS_TOKEN)


def get_project_by_id(project_id: str):
    response = requests.get("{base_url}/projects/{project_id}".format(
        base_url=GITLAB_REST_ENDPOINT, project_id=project_id), headers=GITLAB_REQUEST_HEADERS)
    return response.json()


def get_project_pipelines(project_id: str, ref: str = "master", page=1):
    params = {"order_by": "id",
              "sort": "desc", "per_page": 100, "page": page, "ref": ref}
    response = requests.get("{base_url}/projects/{project_id}/pipelines".format(
        base_url=GITLAB_REST_ENDPOINT, project_id=project_id), headers=GITLAB_REQUEST_HEADERS, params=params)
    return response.json()


def get_pipeline_by_id(project_id: str, pipeline_id: str):
    response = requests.get("{base_url}/projects/{project_id}/pipelines/{pipeline_id}".format(
        base_url=GITLAB_REST_ENDPOINT, project_id=project_id, pipeline_id=pipeline_id), headers=GITLAB_REQUEST_HEADERS)
    return response.json()


def get_project_jobs(project_id: str, page=1):
    params = {"order_by": "id",
              "sort": "desc", "per_page": 100, "page": page}
    response = requests.get("{base_url}/projects/{project_id}/jobs".format(
        base_url=GITLAB_REST_ENDPOINT, project_id=project_id), headers=GITLAB_REQUEST_HEADERS, params=params)
    return response.json()


def get_job_by_id(project_id: str, job_id: str):
    response = requests.get("{base_url}/projects/{project_id}/jobs/{job_id}".format(
        base_url=GITLAB_REST_ENDPOINT, project_id=project_id, job_id=job_id), headers=GITLAB_REQUEST_HEADERS)
    return response.json()
