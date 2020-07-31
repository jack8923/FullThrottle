import pandas as pd
from collections import defaultdict
from pprint import pprint
import ast

from FullThrottle.project.models import Members, Activity_Periods


def defaultvalue():
    return -1


DB_ACTIVITY_PERIODS = defaultdict(defaultvalue)


def add_members_data():
    print("Adding Members CSV to DB")
    members_data = pd.read_csv("")  # Path to CSV File
    print("Data Shape", members_data.shape)
    cnt = 1
    passed_cnt = 0
    for index, row in members_data.iterrows():
        print("Cnt:", cnt)
        cnt += 1
        try:
            curr_member, is_created = Members.objects.get_or_create(real_name=str(row['real_name']), tz=str(row['tz']))
        except:
            print("Member Continuing")
            passed_cnt += 1
            continue
        print("Member Created")

        for val in row['activity_periods']:
            Activity_Periods.objects.get_or_create(member=curr_member, start_time=val['start_time'], end_time=val['end_time'])
    print("Passed No.:", passed_cnt)
    print('-' * 25, "DONE", '-' * 25, sep="")


if __name__ == "__main__":
    add_members_data()
