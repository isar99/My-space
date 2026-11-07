IFS= read -r MYSQL_OLD_PASS <<'PASS'
"T0uchStone_123"
PASS
IFS= read -r MYSQL_NEW_PASS <<'PASS'
"T0uchStone_123!kR8#nQ2wX5pLm9z"
PASS
IFS= read -r MONGO_OLD_PASS <<'PASS'
"T0uchStone_123"
PASS
IFS= read -r MONGO_NEW_PASS <<'PASS'
"T0uchStone_123!kR8#nQ2wX5pLm9z"
PASS
export MYSQL_OLD_PASS MYSQL_NEW_PASS MONGO_OLD_PASS MONGO_NEW_PASS



mysql_new=$(python3 - <<'PY'
import os
import subprocess
import sys


def run(cmd, **kwargs):
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        **kwargs
    )

    if proc.returncode:
        sys.stderr.write(proc.stderr or proc.stdout or "")
        raise SystemExit(proc.returncode)

    return proc


mysql_old = os.environ["MYSQL_OLD_PASS"]
mysql_new = os.environ["MYSQL_NEW_PASS"]

# Escape for MySQL string literal
mysql_pw = mysql_new.replace("\\", "\\\\").replace("'", "''")

sql = (
    "ALTER USER 'touchstoneUser'@'localhost' "
    f"IDENTIFIED BY '{mysql_pw}';\n"
    "ALTER USER 'touchstoneMgmtUser'@'localhost' "
    f"IDENTIFIED BY '{mysql_pw}';\n"
    "ALTER USER 'root'@'localhost' "
    f"IDENTIFIED BY '{mysql_pw}';\n"
    "FLUSH PRIVILEGES;\n"
)

run(
    ["mysql", "-u", "root", f"-p{mysql_old}"],
    input=sql
)

print(mysql_new)
PY
)



mysql -uroot -pT0uchStone_123
ALTER USER 'touchstoneUser'@'localhost' IDENTIFIED BY 'T0uchStone_123!kR8#nQ2wX5pLm9z';
ALTER USER 'touchstoneMgmtUser'@'localhost' IDENTIFIED BY 'T0uchStone_123!kR8#nQ2wX5pLm9z';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'T0uchStone_123!kR8#nQ2wX5pLm9z';



mongo_new=$(python3 - <<'PY'
import json
import os
import subprocess
import sys


def run(cmd, **kwargs):
    proc = subprocess.run(
        cmd, capture_output=True, text=True, **kwargs
    )
    if proc.returncode:
        sys.stderr.write(proc.stderr or proc.stdout or "")
        raise SystemExit(proc.returncode)
    return proc


mongo_old = os.environ["MONGO_OLD_PASS"]
mongo_new = os.environ["MONGO_NEW_PASS"]
quoted = json.dumps(mongo_new)
js = (
    f"db.changeUserPassword('touchstoneUser', {quoted});\n"
    f"db.changeUserPassword('admin', {quoted});\n"
)
run(
    ["mongosh", "admin", "-u", "admin", f"--password={mongo_old}"],
    input=js,
)
print(mongo_new)
PY
)

mongosh admin -u admin --password=T0uchStone_123
db.changeUserPassword('touchstoneUser', 'T0uchStone_123!kR8#nQ2wX5pLm9z');
db.changeUserPassword('admin', 'T0uchStone_123!kR8#nQ2wX5pLm9z');


echo "$mysql_new"
echo "$mongo_new"

sudo MYSQL_NEW_PASS="$mysql_new" MONGO_NEW_PASS="$mongo_new" python3 - <<'PY'
import configparser
import os

config_file = "/etc/touchstone/db.conf"

config = configparser.ConfigParser()
config.read(config_file)

config["touchstone_mongodb"]["password"] = os.environ["MONGO_NEW_PASS"]
config["touchstone_mysql"]["password"] = os.environ["MYSQL_NEW_PASS"]

with open(config_file, "w") as f:
    config.write(f)
PY




python3 - <<'PY'
import os
import subprocess
import sys


def run(cmd, **kwargs):
    proc = subprocess.run(
        cmd, capture_output=True, text=True, **kwargs
    )
    if proc.returncode:
        sys.stderr.write(proc.stderr or proc.stdout or "")
        raise SystemExit(proc.returncode)
    return proc


db = "/etc/touchstone/db.conf"
mysql_pw = os.environ["MYSQL_NEW_PASS"]
mongo_pw = os.environ["MONGO_NEW_PASS"]
for section, password in (
    ("touchstone_mysql", mysql_pw),
    ("touchstone_mongodb", mongo_pw),
    ("management_mysql", mysql_pw),
):
    run(
        [
            "sudo", "crudini", "--set", db, section, "password",
            password,
        ],
    )

for section, env in (
    ("touchstone_mysql", "MYSQL_NEW_PASS"),
    ("touchstone_mongodb", "MONGO_NEW_PASS"),
    ("management_mysql", "MYSQL_NEW_PASS"),
):
    expected = os.environ.get(env, "")
    actual = run(
        ["sudo", "crudini", "--get", db, section, "password"],
    ).stdout.rstrip("\n")
    if not actual:
        print(f"{section} = EMPTY")
    elif actual == expected:
        print(f"{section} = OK")
    else:
        print(f"{section} = MISMATCH")
PY

