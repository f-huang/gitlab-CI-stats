import pytz

from iso8601 import parse_date
from gitlab_api import get_project_pipelines, get_pipeline_by_id
from datetime import datetime


def get_pipelines_by_date(project_id: str, start_date: str):
    start_date = datetime.strptime(
        start_date, "%Y-%m-%d").replace(tzinfo=pytz.utc)
    page = 1
    last_date_found = None
    pipelines = []
    while ((last_date_found is None or last_date_found > start_date)):
        pipelines = [*pipelines, *(
            get_project_pipelines(project_id, page=page))]
        last_date_found = parse_date(pipelines[-1]["created_at"])
        page += 1

    print("number of pages queried {}".format(page))
    return pipelines


def hydrate_pipelines(project_id: str, pipelines):
    i = 0
    while i < len(pipelines):
        pipelines[i] |= get_pipeline_by_id(project_id, pipelines[i]["id"])
        i += 1
    return pipelines
