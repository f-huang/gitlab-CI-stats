import pytz
import datetime

from iso8601 import parse_date
from gitlab_api import get_project_jobs, get_job_by_id


def get_jobs_by_date(project_id: str, start_date: datetime.date):
    start_date = datetime.datetime(
        start_date.year, start_date.month, start_date.day).replace(tzinfo=pytz.utc)
    page = 1
    last_date_found = None
    jobs = []
    while ((last_date_found is None or last_date_found > start_date)):
        jobs = [*jobs, *(
            get_project_jobs(project_id, page=page))]
        last_date_found = parse_date(jobs[-1]["created_at"])
        page += 1

    print("number of pages queried {}".format(page))
    return jobs


def hydrate_jobs(project_id: str, jobs):
    i = 0
    while i < len(jobs):
        jobs[i] |= get_job_by_id(project_id, jobs[i]["id"])
        i += 1
    return jobs
