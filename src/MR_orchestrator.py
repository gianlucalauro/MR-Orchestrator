import os
import platform
import random
import subprocess
from utils import get_unused_profiles
from utils import refresh_csv
from utils import base_path


unused_profiles = get_unused_profiles()

if unused_profiles:
    # get a random one
    selected_profile = random.choice(unused_profiles)

    # execute the script with the selected profile
    if platform.system() == "Linux":
        subprocess.Popen(["bash", os.path.join(base_path, "scripts", "startChromium.sh"), selected_profile, "&"])

    if platform.system() == "Windows":
        subprocess.Popen([os.path.join(base_path, "scripts", "startChromium.bat"), selected_profile])

    # once all is done, refresh the csv
    refresh_csv(selected_profile)
