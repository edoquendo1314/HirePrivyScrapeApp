import requests
from collections.abc import MutableMapping
from dotenv import load_dotenv
from proxycurl_py.asyncio import Proxycurl
import os
import json
import asyncio

# proxycurl = Proxycurl()

load_dotenv()

class ProxyCurlAPI:

    linkedin_profile_url = 'https://www.linkedin.com/in/temp-hire-163aa7266/'
    company_search_endpoint = os.getenv("API_ENDPOINT_COMPANY_SEARCH")
    api_key = os.getenv("PROXY_API_KEY")
    header_dic = {'Authorization': 'Bearer ' + api_key}
    client_url = ""
    client_info = ""

    def __init__(self, company_name):
        self.company_name = company_name
    
    ##\bHR\sManager\b
    ##\bExecutive\sDirector\b
    ## obtain employee url
    ##search for HR and Exec
    def employee_search(self, page_size, regex_title):

        params = {
            'page_size': f'{page_size}',
            'linkedin_company_profile_url': f'https://www.linkedin.com/company/{self.company_name}/',
            'keyword_regex': f'{regex_title}',
        }
        try:
            r = requests.get(self.company_search_endpoint,
                            params = params, 
                            headers = self.header_dic)

            self.client_url = r.json()
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return self.client_url
    
    ##Webhook eventually for this method
    ##obtain email
    def work_email_lookup(self, linkedin_profile_url):
        params = {
            'linkedin_profile_url':'https://www.linkedin.com/in/kayla-kruse-80a05441/',
            'callback_url': 'https://webhook.site/ad8741c9-0bcd-4e5d-9ccd-e37aba558c5a',
        }
        try:
            r = requests.get(os.getenv("API_ENDPOINT_EMAIL"),
                        params = params,
                        headers = self.header_dic)
            ##webhook response
            print(r.text)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return r.json()
    
    ##obtain client information for contact creation
    def client_info_lookup(self, linkedin_profile_url):
        params = {
            'url': f'{linkedin_profile_url}',
            'fallback_to_cache': 'on-error',
            'use_cache': 'if-present',
            'skills': 'exclude',
            'inferred_salary': 'exclude',
            'personal_email': 'include',
            'personal_contact_number': 'include',
            'twitter_profile_id': 'exclude',
            'facebook_profile_id': 'exclude',
            'github_profile_id': 'exclude',
            'extra': 'exclude',
        }
        try:
            r = requests.get(os.getenv("API_ENDPOINT_LINKEDIN"),
                        params = params,
                        headers = self.header_dic)
            self.client_info = json.loads(r.json())
            print(r.json)
            r.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
        return self.client_info




