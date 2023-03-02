import requests
from collections.abc import MutableMapping
from dotenv import load_dotenv
import os
import json

# app = Flask(__name__)

load_dotenv()


class TrackerRMSAPI:
    endpoint = os.getenv("TRACKER_ENDPOINT_US")
    signIn = os.environ.get('SIGN_IN_ACCOUNT')
    password = os.environ.get('PASS')
    # api_key = ''
    # header_dic = {'Authorization': 'Bearer ' + api_key}
    
    def __init__(self, data):
        self.data = data
    
    #change to oAUTH2
    def createResource(self):
        data = {
                    "trackerrms": {
                            "createResource": {
                                    "credentials": {
                                        "username": f'{self.signIn}',
                                        "password": f'{self.password}',
                                    },
                                    "instructions": {
                                        "overwriteresource": 'false',
                                        "assigntoopportunity": 1654,
                                        "assigntolist": 'short',
                                        "shortlistedby": 'resource'
                                    },
                                    "resource": {
                                        "firstname": "Jane",
                                        "lastname": "Selby",
                                        "fullname": "Jane Selby",
                                        "jobtitle": "Java Programmer",
                                        "company": "Wonderful Java Inc",
                                        "address1": "2245 Jasper Lane",
                                        "address2": "Del Mar",
                                        "city": "San Diego",
                                        "state": "CA",
                                        "zipcode": "92367",
                                        "country": "United States",
                                        "workphone": "",
                                        "homephone": "555-3748",
                                        "cellphone": "888-3487",
                                        "email": "jane.selby@gmailx.com",
                                        "linkedin": "https://linkedin.com/jsca/",
                                        "dateofbirth": "1984-04-28",
                                        "nationality": "United States",
                                        "languages": "French, English",
                                        "education": "Master’s Degree",
                                        "source": "Website",
                                        "jobhistory": [
                                                {
                                                "company": "Wonderful Java Inc.",
                                                "jobtitle": "Java Programmer",
                                                "startdate": "2016",
                                                "enddate": "",
                                                "description": "I programmed Java"
                                                },
                                                {
                                                "company": "Another Company",
                                                "jobtitle": "Junior JS Developer",
                                                "startdate": "2013",
                                                "enddate": "2017",
                                                "description": "Graduate developer"
                                                }
                                        ],
                                        "salary": 33000,
                                        "note": "Lorem ipsum dolor sit amet.",
                                        "image": "http://url.to.image",
                                        "skills": "123,456,789,654",
                                        "status": "Active",
                                        "customfields": [
                                                {
                                                "id": 123,
                                                "value": "Value 1"
                                                },
                                                {
                                                "id": 456,
                                                "value": "Value 2"
                                                }
                                        ]
                                    }
                            }
                    }
        }
        try:
            # request = self.endpoint + '/api/widget/createResource'

            r = requests.post(
                self.endpoint,
                json=data,
            )
            print(r.json())
            return r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)


    def createContact(self):
        data = {
                    "trackerrms": {
                        "createContact": {
                                "credentials": {
                                    "username": f'{self.signIn}',
                                    "password": f'{self.password}',
                                    "oauthtoken": "",
                                },
                                "instructions": {
                                    "createcompanyifnotexists": 'true',
                                    "overwritecontact": 'false'
                                },
                                "contact": {
                                    "firstname": "Thomas",
                                    "lastname": "Johnson",
                                    "fullname": "Thomas Johnson",
                                    "jobtitle": "Managing Director",
                                    "company": "ABC Incorporated",
                                    "address1": "2567 Lexington Avenue",
                                    "address2": "",
                                    "city": "New York",
                                    "state": "NY",
                                    "zipcode": "10263",
                                    "country": "United States",
                                    "businessphone": "555-2387",
                                    "homephone": "",
                                    "cellphone": "888-3465",
                                    "email": "john.brown@abcincorp.com",
                                    "linkedin": "https://linkedin.com/jbabc/",
                                    "website": "",
                                    "note": "Testing",
                                    "image": "http://url.to.image"
                                }
                        }
                    }
        }
  
        try:
            endpoint = 'https://evoapius.tracker-rms.com/api/widget/createContact/'
            r = requests.post(
                endpoint,
                json=data,
            )
            print(r.json())
            return r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)

        

    # def auth(self):
    #     request = self.endpoint + '/oAuth2/Authorize'
    #     params = {
    #         'client_id': 'EvoApi_1.0',
    #         'response_type': 'code',
    #         'scope': 'read,write',
    #         'redirect_uri': 'https://localhost:8080/callback',
    #         'state': 'djfal9kmn23dkfu!214',
    #     }
    #     try:
    #         r = requests.get(request, params)
    #         # self.api_key = r.json()
    #         print(r.json)
    #         result = Flask.redirect(url_for("/callback"))
    #         print(result.json())
    #         r.raise_for_status()
    #     except requests.exceptions.HTTPError as errh:
    #         print ("Http Error:",errh)
    #     except requests.exceptions.ConnectionError as errc:
    #         print ("Error Connecting:",errc)
    #     except requests.exceptions.Timeout as errt:
    #         print ("Timeout Error:",errt)
    #     except requests.exceptions.RequestException as err:
    #         print ("OOps: Something Else",err)
    

    # def authToken(self):
    #     params = {
    #         'client_id': 'EvoApi_1.0',
    #         'redirect_uri': 'https://localhost:8081',
    #         'grant_type': f'{self.api_key}',
    #         'client_secret': '',
    #         'code': '',
    #         'refresh_token':'https://localhost:8080',
    #     }



    # @app.route("/callback")
    # def callback():
    #     return 'success'

# if __name__ == '__main__':
#    app.run(debug = True)

obj = TrackerRMSAPI(1)
obj.createContact()
print(obj.password)
print(obj.signIn)