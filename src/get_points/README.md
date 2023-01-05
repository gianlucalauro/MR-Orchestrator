# Get Points Plugin
This plugin is used to get actual points for each profile

Without touching [**profiles.csv**](../../profiles.csv), the table will be like:

|Profiles|Last_Farm_Date| Points |
|---------|-----|--------|
|Profile 1|2022-04-12 00:12:53|9.036|
|Profile 2|2022-04-12 00:12:51|7.500|
|Profile 3|2022-04-12 00:12:56|26.192|


## Guide

0) If not installed the dependencies, just execute: `pip install -r requirements.txt`

1) Change [**chrome-user-data-dir.txt**](chrome-user-data-dir.txt) with your chrome user data folder path
> For example: 
> - In Linux: /home/&lt;*user*&gt;/.config/chromium/
> - In Windows: C:\\Users\\&lt;*user*&gt;\\AppData\\Local\\Google\\Chrome\\User Data\\

2) Before execute [**get_points.py**](get_points.py) check if all chrome instances are closed