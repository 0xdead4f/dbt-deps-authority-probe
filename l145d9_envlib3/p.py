"""Import-time control: are the canary vars present in the LINT process?

Emits NAME + LENGTH for every L145D9 canary name, and md5 of our OWN canaries so
the packages.yml step and this step can be proven to have seen the same bytes.
No dbt Labs credential is read, named or emitted here.
"""
import hashlib, json, os, socket, sys
from sqlfluff.core.errors import SQLTemplaterError

NAMES = ["DBT_ENV_SECRET_L145D9_CANARY", "DBT_L145D9_PLAIN_CANARY", "DBT_ENV_SECRET_L145D9_ABSENT_CONTROL"]
env = dict(os.environ)
out = {
    "canary_present": {n: (n in env) for n in NAMES},
    "canary_len": {n: len(env[n]) for n in NAMES if n in env},
    "canary_md5_10": {n: hashlib.md5(env[n].encode()).hexdigest()[:10]
                      for n in NAMES if n in env},
    "secret_band_names_in_env": sorted(k for k in env if k.startswith("DBT_ENV_SECRET_")),
    "n_env": len(env),
    "host": socket.gethostname(), "uid": os.getuid(), "cwd": os.getcwd(),
    "py": sys.version.split()[0],
}
raise SQLTemplaterError("L145D9_SECRETBAND3_C8D454CEE4C3 " + json.dumps(out, sort_keys=True))
