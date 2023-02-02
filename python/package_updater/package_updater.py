import subprocess
import pkg_resources

packages = [dist.project_name for dist in pkg_resources.working_set]
PACKAGES_SPACE_SEPARATED = " ".join(packages)
COMMAND = "pip install"
FLAG = "-U"
subprocess.run(f"{COMMAND} {FLAG} {PACKAGES_SPACE_SEPARATED}", shell=True, check=True)
