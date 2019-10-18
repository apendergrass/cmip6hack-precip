"""This is a general purpose module containing routines
(a) that are used in multiple notebooks; or 
(b) that are complicated and would thus otherwise clutter notebook design.
"""

import re
import socket
import intake

def is_ncar_host():
    """Determine if host is an NCAR machine."""
    hostname = socket.getfqdn()
    
    return any([re.compile(ncar_host).search(hostname) 
                for ncar_host in ['cheyenne', 'casper', 'hobart']])

def load_data_catalog():
    """Load data on either NCAR or pangeo machine."""
    if is_ncar_host():
        col = intake.open_esm_datastore("../catalogs/glade-cmip6.json")
    else:
        col = intake.open_esm_datastore("../catalogs/pangeo-cmip6.json")
    return col