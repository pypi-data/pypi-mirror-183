import getpass
import os

def get_current_pac():
    user = getpass.getuser()
    return user.split('-')[0]


def get_users_of_pac(pac):
    if not os.path.isdir(f'/home/pacs/{pac}/users'):
        return None

    result = []
    for f in os.scandir(f'/home/pacs/{pac}/users'):
        if f.is_dir():
            result.append(f.name)

    return result

