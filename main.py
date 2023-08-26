from bs4 import BeautifulSoup
import requests
import os

def emptyPostsDir(directory_path):
    file_list = os.listdir(directory_path)

    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

print("enter a skill that you are not familiar with")
unfamiliar_skills = input(">").split(" ")
print(f"filtering out {unfamiliar_skills}...")
print("")

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml")
jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

emptyPostsDir("./posts")
count = 0
for index, job in enumerate(jobs):
    publish_date = job.find("span", class_="sim-posted").span.text
    if "few" in publish_date:
        company_name = job.find("h3", class_="joblist-comp-name").text.strip()
        skills = [skill.strip() for skill in job.find("span", class_="srp-skills").text.strip().split(",")]
        more_info = job.header.h2.a['href']
        unf = False
        for unfamiliar_skill in unfamiliar_skills:
            if unfamiliar_skill in skills:
                unf = True
        if not unf:
            count+=1
            with open(f"posts/{count}.txt", "w") as f:
                f.write(f"comapany: {company_name}\n")
                f.write(f"skills: {skills}\n")
                f.write(f"more_info: {more_info}\n")

print(f"found {count} jobs")