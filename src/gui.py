from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import time
import os
import json

from src.octoparsescraper import Octoparse
from src.proxycurl import ProxyCurlAPI
from src.checkcompany import CompanyValidity

Builder.load_file('appArchitecture.kv')

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class MyGridLayout(Widget):
    job_title = ObjectProperty(None)
    region_id = ObjectProperty(None)
    loadfile = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        file_path = os.path.join(path, filename[0])
        list_result = Octoparse(file_path)
        company_list = list_result.__readFile__()
        ##make sure all companies are lower case before sending
        proxy_result = ProxyCurlAPI(company_name='microsoft')
        #client_url = proxy_result.employee_search(page_size=5, regex_title='HR Manager')
        #client_info = proxy_result.client_info_lookup(linkedin_profile_url=client_url)
        client_email = proxy_result.work_email_lookup("https://www.linkedin.com/in/williamhgates")
        #print(client_email)
        ##print(webhook_response.webhook)
        ###create contact


        ##add this
        # company_list = CompanyValidity(company_list)

        # for companies in company_list:
        #     ProxyCurlAPI(companies)
        #     time.sleep(5)
        
        self.dismiss_popup()
    
    def spinner_clicked(self, value):
        region_id = self.region_id.text
        print(region_id)
        region_id = ObjectProperty(None)
        ## based on region forward geo id
        print(region_id)

class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()
    



# def press(self):
    #     job_title = self.ids.job_title.text
    #     self.job_title.text = ""