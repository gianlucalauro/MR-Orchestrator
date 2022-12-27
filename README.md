# MR Orchestrator
This project is used for claim daily MR points for many accounts

## Requirements
- Python
- Chromium
- NordVPN - CLI


## Guide
Once you have cloned this repo:

0) Install dependencies with: `pip install -r requirements.txt`

1) Create N profiles in chromium.

2) For each profile, install ABS and login on Bing and MR Rewards dashboard.
	> **Note:** use the vpn for each profile when you have to login

3) In **profiles.csv** set the correct profile names in the first column.
- example:

|Profiles|Last_Farm_Date|
|---------|-----|
|Profile 1|2022-04-12 00:12:53|
|Profile 2|2022-04-12 00:12:51|
|Profile 3|2022-04-12 00:12:56|
> **Note:** the profile name must be the same as the one created in chromium. You can see that in the config subfolder of chromium. For example: `~/.config/chromium`

4) With a scheduler program (for example, crontab) run the **MR_orchestrator.py** script like this:
	- `0,30 * * * * python path/to/MR_orchestrator.py`
	<sup>this means "run when the minute of each hour  **is 0 or 30**" (would run at: 1:30, 2:00, 2:30, 3:00, etc)</sup>