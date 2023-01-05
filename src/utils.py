import pandas as pd
from datetime import datetime
from os.path import dirname, abspath, join

base_path = dirname(dirname(abspath(__file__)))
path_to_CSV = join(base_path, "profiles.csv")

date_format = '%Y-%m-%d %H:%M:%S'

all_profiles = pd.read_csv(path_to_CSV)


def get_unused_profiles():
    func_unused_profiles = []
    for profile, timestamp in zip(all_profiles.Profiles, all_profiles.Last_Farm_Date):
        if datetime.strptime(timestamp, date_format).date() < datetime.today().date():
            func_unused_profiles.append(profile)

    return func_unused_profiles


def refresh_csv(selected_profile):
    all_profiles.loc[all_profiles.Profiles == selected_profile, 'Last_Farm_Date'] = datetime.now().strftime(date_format)
    all_profiles.to_csv(path_to_CSV, index=False)


def get_all_profiles():
    return list(all_profiles.Profiles)


def write_points(profile, points):
    all_profiles.loc[all_profiles.Profiles == profile, 'Points'] = points
    all_profiles.to_csv(path_to_CSV, index=False)
