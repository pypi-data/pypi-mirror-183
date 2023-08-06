import os, subprocess
import hsutilities.users as hsusers

def get_subdomains_of_domain(user, domain):

    path = "~/doms/{domain}/subs-ssl"
    stream = os.popen(f'sudo -u {user} -s /bin/bash -c "if [ -d {path} ]; then ls -1 {path}; fi"')
    subdomains = stream.read()
    if subdomains:
        return subdomains.split('\n')
    return None


def get_domains_of_user(user):

    result = {}
    cmd = "if [ -d ~/doms ]; then ls ~/doms -1; fi"
    output = subprocess.getoutput(f'sudo -u {user} -s /bin/bash -c "{cmd}"').split('\n')
    for line in output:
        if line:
            result[line] = {'domain': line, 'user': user}
    return result


def get_domains_of_pac(pac):

    result = {}

    result = get_domains_of_user(pac)
    users = hsusers.get_users_of_pac(pac)
    for user in (users or []):
        result.update(get_domains_of_user(f"{pac}-{user}"))

    return result

