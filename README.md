__#instagram-not-following-back-analysis__

this project analyses your followers and following (which you previously downloaded from instagram) 
and gives you a list of usernames that you follow but don’t follow you back. 

__#Table of contents__

_-[Preparation] #preparation_ 

_-[Usage]#usage_



__#preparation__

first you have to download your profile information from instagram. To do this go to your meta profile and click
on "your information and permissions". You should see an option to download your data now. Create an export and 
choose to export it on to your own device. Adjust the information such that you only download your contacts 
(followers and following) and uncheck the rest of the information, you won’t be needing it. For the time period 
click on all time. The format is irrelevant since I provided a script for both html and json. 

-> when the information is ready to download, do so and make sure that the followers list and following list 
are in the same file as both of the python scripts.

__#usage__ 

to get the script to run just navigate to the file in the terminal and run the command:
python3 ig_not_following_back.py for json or python3 ig_not_following_back_html.py for html



