import requests
import json


def get_api_data():
  url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/vaccines/get-all-vaccines-phase-iv"

  headers = {
      'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
      'x-rapidapi-key': "61b6ce0b76msh81422ad5dc23da9p183374jsn5dce178c59bb"
  }

  response = requests.request("GET", url, headers=headers)
  #print(response.text)
  jsonData = json.loads(response.text)

  #print(json.dumps(jsonData, indent=2))
  print(jsonData[4]['description'])
