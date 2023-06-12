import requests

response = requests.get("https://gitlab.com/api/v4/users/ahmedabed/projects")
my_projects = response.json()

for project in my_projects:
    print(f"project name is {project['name']} and url is {project['http_url_to_repo']}")