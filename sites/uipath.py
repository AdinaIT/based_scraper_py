from scraper_peviitor import Scraper, loadingData
import uuid
import json

apiUrl = "https://careers.uipath.com/api/jobs?location=romania&stretch=50&stretchUnit=MILES&page=1&limit=100&country=Romania&sortBy=relevance&descending=false&internal=false"

scraper = Scraper(apiUrl)

jobs = scraper.getJson().get("jobs")

company = {"company": "UiPath"}
finalJobs = list()

for job in jobs:
    job = job.get("data")

    id = uuid.uuid4()
    job_title = job.get("title")
    job_link = job.get("meta_data").get("canonical_url")
    city = job.get("city")

    finalJobs.append({
        "id": str(id),
        "job_title": job_title,
        "job_link": job_link,
        "company": company.get("company"),
        "country": "Romania",
        "city": city
    })

print(json.dumps(finalJobs, indent=4))

loadingData(finalJobs, company.get("company"))