import argparse
import datetime

from gitlab_pipelines import get_pipelines_by_date, hydrate_pipelines
from gitlab_jobs import get_jobs_by_date, hydrate_jobs
from csv_writer import write_pipelines_to_csv

if __name__ == '__main__':
    print("Hello World !")

    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", type=int, help="GitLab's project id")
    parser.add_argument("resource", type=str,
                        help="GitLab's resource to query: 'job' or 'pipeline'")
    parser.add_argument("--until_date", required=True, type=datetime.date.fromisoformat,
                        help="Get pipelines until a certain date. Format YYYY-MM-DD")
    parser.add_argument("--output_filepath",  type=str, default="pipelines.csv",
                        help="Output filepath of csv")
    args = parser.parse_args()

    if (args.resource == "pipelines"):
        pipelines = get_pipelines_by_date(args.project_id, args.until_date)
        pipelines = hydrate_pipelines(args.project_id, pipelines)
        write_pipelines_to_csv(args.output_filepath, pipelines)
    elif args.resource == "jobs":
        jobs = get_jobs_by_date(args.project_id, args.until_date)
        jobs = hydrate_jobs(args.project_id, jobs)
        write_pipelines_to_csv(args.output_filepath, jobs)
    print("results stored at {}".format(args.output_filepath))
