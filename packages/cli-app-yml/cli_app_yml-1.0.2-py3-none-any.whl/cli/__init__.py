import os
import sys

sys_paths = [
    os.path.dirname(__file__),
    "minion",
    ".tmp"
]
def import_syspaths(paths):
    for p in paths:
        sys.path.append(p)

from .cli import Cli
import_syspaths(sys_paths)

def run():
    from dotenv import load_dotenv
    
    cwd = os.getcwd()
    load_dotenv(dotenv_path=cwd + "/.env")
    # for e in os.environ:
    #     print(e)
    
    try:
        cli_man = Cli(os.environ.get("CLI_CONFIG", "cli.yml"))
        cli_man.run()
    finally:
        Cli.cleanup()