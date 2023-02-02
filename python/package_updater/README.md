# Package Updater
This script updates all the packages in the current Python environment using pip. It uses the `pkg_resources` library to get a list of all the packages in the current environment and then passes this list as an argument to the `pip install` command with the `-U` flag to indicate upgrade. The `subprocess.run` method is used to run this shell command.
