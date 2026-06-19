import os
from dotenv import load_dotenv


load_dotenv() 


PROJECT_ID = os.getenv("PROJECT_ID")
TOKEN = os.getenv("GITLAB_TOKEN")
GITLAB_URL = "https://gitlab.com/api/v4"

HEADERS = {
    "PRIVATE-TOKEN": TOKEN
}

def get_latest_failed_pipeline():
    """Project ki sabse latest fail hui pipeline dhundhta hai."""
    url = f"{GITLAB_URL}/projects/{PROJECT_ID}/pipelines?status=failed"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200 and response.json():
        latest_pipeline = response.json()[0]
        print(f"❌ Failed Pipeline Found! ID: {latest_pipeline['id']}")
        return latest_pipeline['id']
    else:
        print("✅ No failed pipelines found or API error.")
        return None

def get_failed_job_log(pipeline_id):
    """Us fail hui pipeline ke error logs (trace) nikalta hai."""
    url = f"{GITLAB_URL}/projects/{PROJECT_ID}/pipelines/{pipeline_id}/jobs"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        jobs = response.json()
        for job in jobs:
            if job['status'] == 'failed':
                job_id = job['id']
                print(f"🔍 Fetching logs for failed job: {job_id}")
                
                # Fetching the actual error log
                log_url = f"{GITLAB_URL}/projects/{PROJECT_ID}/jobs/{job_id}/trace"
                log_response = requests.get(log_url, headers=HEADERS)
                return log_response.text
    return "No logs found."

# Testing the code
if __name__ == "__main__":
    p_id = get_latest_failed_pipeline()
    if p_id:
        error_log = get_failed_job_log(p_id)
        print("\n--- ERROR LOG EXTRACTED ---")
        
        print(error_log[-500:])