import json

request = HttpRequest({'url': valueProvider.jiraServer.url}, valueProvider.jiraServer.username, valueProvider.jiraServer.password)
response = request.get("/rest/api/2/project", contentType = 'application/json')
data = json.loads(response.getResponse())
result = []
for repository in data:
    result = result + [repository['key']]