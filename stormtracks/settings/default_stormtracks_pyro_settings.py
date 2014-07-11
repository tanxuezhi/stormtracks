# *** DON'T MODIFY THIS FILE! ***
#
# Instead copy it to stormtracks_pyro_settings.py
# 
# Default settings for project
# This will get copied to $HOME/.stormtracks/
# on install.
import socket

hostname = socket.gethostname()

if len(hostname.split('.')) >= 2:
    is_ucl = True
    nameserver = 'madrid'
    ssh_kill_cmd_tpl = 'ssh {0} "bash DATA/stormtracks/bin/kill_pyro.sh"'
    ssh_start_cmd_tpl = 'ssh {0} "cd /home/ucfamue/DATA/stormtracks/pyro_cluster && /opt/anaconda/bin/python pyro_worker.py &" &'

    manager = 'madrid'
    worker_servers = [
    'berlin', 
    'warsaw', 
    'naples', 
    'vienna', 
    'venice', 
    'prague', 
    #'lisbon', 
    'dublin', 
    'rome', 
    'oslo', 
    'athens', 
    'cologne', 
    'mainz', 
    'linz', 
    'seville', 
    'bergen', 
    'granada', 
    'cordoba', 
    'zurich', 
    'leipzig', 
    'riga', 
    'vilnius', 
    'tallinn', 
    'salzburg', 
    'antwerp', 
    'budapest', 
    'helsinki', 
    'munich', 
    'nice', 
    'turin', 
    'marseille'] 
    worker_servers = worker_servers[:2]
else:
    is_ucl = False
    nameserver = '192.168.0.15'
    ssh_kill_cmd_tpl = 'ssh {0} "bash Projects/stormtracks/bin/kill_pyro.sh"'
    ssh_start_cmd_tpl = 'ssh {0} "cd /home/markmuetz/Projects/stormtracks/pyro_cluster && python pyro_worker.py &" &'
    manager = 'breakeven-mint'
    worker_servers = ['determinist-mint']
