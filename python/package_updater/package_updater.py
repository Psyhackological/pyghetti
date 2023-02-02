"""
This module contains only main function
"""
import subprocess
import pkg_resources


def main():
    """
    This script updates all the packages in the current Python environment using pip.
    """
    distributions = list(pkg_resources.working_set)
    packages = [dist.project_name for dist in distributions]
    packages_space_separated = " ".join(packages)
    command = "pip install"
    flag = "-U"
    subprocess.run(
        f"{command} {flag} {packages_space_separated}", shell=True, check=True
    )


if __name__ == "__main__":
    main()
