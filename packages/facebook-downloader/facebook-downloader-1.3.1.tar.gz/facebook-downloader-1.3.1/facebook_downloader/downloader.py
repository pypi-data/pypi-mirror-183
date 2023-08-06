import os
import argparse
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
 

class FacebookDownloader:
    def __init__(self):
        parser = argparse.ArgumentParser(description='facebook-downloader — by Richard Mwewa')
        parser.add_argument('url', help='facebook video url (eg. https://www.facebook.com/PageName/videos/VideoID')
        parser.add_argument('-a', '--audio', help='download file as audio', action='store_true')
        parser.add_argument('-o', '--output', help='output filename')
        self.args = parser.parse_args()

        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        self.driver = webdriver.Firefox(options=option)

        self.program_version_number = "1.3.1"
        self.downloading_url = "https://getfvid.com"
        self.update_check_endpoint = "https://api.github.com/repos/rly0nheart/facebook-downloader/releases/latest"
        
        
    def notice(self):
        return f"""
        facebook-downloader v{self.program_version_number} Copyright (C) 2023  Richard Mwewa
        
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
        """
        
        
    def check_updates(self):
        print(self.notice())
        response = requests.get(self.update_check_endpoint).json()
        if response['tag_name'] == self.program_version_number:
            """Ignore if the program is up to date"""
            pass
        else:
            print(f"[UPDATE] A new release is available ({response['tag_name']}). Run 'pip install --upgrade facebook-downloader' to get the updates.")

    
    def download_type(self):
        """
        The elements change according to what file type will be downloaded
        So, we pass an option to specify what file type we want, by default the file is an HD video
        """
        """
        HD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a"
        SD: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[2]/a"
        Audio: "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a"
        """
        if self.args.audio:
            download_type_element = "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[3]/a"
        else:
            download_type_element = "/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[3]/p[1]/a"
        
        return download_type_element


    def path_finder(self):
        os.makedirs("downloads", exist_ok=True)
            
    
    def download_video(self):
        self.path_finder()
        self.check_updates()
        self.driver.get(self.downloading_url) # Opening getfvid.com, a website that downloads facebook videos
        url_entry_field = self.driver.find_element(By.NAME, "url") # Find the url entry field
        url_entry_field.send_keys(self.args.url) # write facebook url in the entry field
        url_entry_field.send_keys(Keys.ENTER) # press enter
        print('[INFO] Loading web resource, please wait...')
        # self.driver.refresh
        
        download_btn = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.XPATH, self.download_type()))) # Find the download button (this clicks the first button which returns a video in hd)
        download_url = download_btn.get_attribute('href')
        
        with requests.get(download_url, stream=True) as response:
            response.raise_for_status()
            with open(os.path.join('downloads', f'{self.args.output}.mp4'), 'wb') as file:
                for chunk in tqdm(response.iter_content(chunk_size=8192), desc=f'[INFO] Downloading: {self.args.output}.mp4'):
                    file.write(chunk)
                print(f'[INFO] Downloaded: {file.name}')
        self.driver.close()
        
