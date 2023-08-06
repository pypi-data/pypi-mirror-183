
import sys
import argparse
import subprocess
import os
import requests
import json
import shutil
import platform
import stat
from . import http

def get_python_link_name(pydll_path, os_name):
    if os_name == "linux":
        for so in os.listdir(pydll_path):
            if so.startswith("libpython") and not so.endswith(".so") and so.find(".so") != -1:
                basename = os.path.basename(so[3:so.find(".so")])
                full_path = os.path.join(pydll_path, so)
                return basename, full_path
    return None, None

class Cmd:
    def __init__(self, actions):
        self.parser    = argparse.ArgumentParser()
        self.subparser = self.parser.add_subparsers(dest="cmd")
        self.actions   = actions

    def add_cmd(self, name : str, help : str = None)->argparse._ActionsContainer:
        return self.subparser.add_parser(name, help=help)

    def help(self):
        self.parser.print_help()

    def run(self):
        args = self.parser.parse_args()
        if args.cmd is None:
            self.help()
            return

        if not self.actions.run(**args.__dict__):
            self.help()
            return


class Config:
    def __init__(self):
        self.SERVER      = "https://www.zifuture.com/api"
        self.CACHE_ROOT  = os.path.expanduser('~/.cache/kiwi')
        self.CACHE_FILE  = os.path.join(self.CACHE_ROOT, "config.json")
        self.OS_NAME     = platform.system().lower()
        self.PY_VERSION  = ".".join(sys.version.split(".")[:2])
        self.KIWI_ROOT   = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))
        self.CWD         = os.path.abspath(os.path.curdir)
        self.PYLIB_DIR   = os.path.join(sys.exec_prefix, "lib")
        self.PYLIB_NAME, self.PYLIB_PATH = get_python_link_name(self.PYLIB_DIR, self.OS_NAME)
        self.DATA_DIR    = os.path.join(self.CACHE_ROOT, "data")
        self.PKG_DIR     = os.path.join(self.CACHE_ROOT, "pkg")
        self.LIB_DIR     = os.path.join(self.CACHE_ROOT, "lib")
        self.CODE_DIR    = os.path.join(self.CACHE_ROOT, "code")
        os.makedirs(self.CACHE_ROOT, exist_ok=True)
        os.makedirs(self.DATA_DIR, exist_ok=True)
        os.makedirs(self.PKG_DIR,  exist_ok=True)
        os.makedirs(self.LIB_DIR,  exist_ok=True)
        os.makedirs(self.CODE_DIR, exist_ok=True)
        
        self.ACCESS_TOKEN = ""
        self.dynamic_keys = [
            "DATA_DIR", "CODE_DIR", "PKG_DIR", "ACCESS_TOKEN", "SERVER"
        ]
        self.setup()

    def load(self):
        if not os.path.exists(self.CACHE_FILE):
            return

        with open(self.CACHE_FILE, "r") as f:
            cfg = json.load(f)
        
        if not isinstance(cfg, dict):
            raise RuntimeError("Config must dict.")
        
        for key in cfg:
            if key in self.dynamic_keys:
                if cfg[key] is not None:
                    setattr(self, key, cfg[key])
            else:
                print(f"Unknow config name {key}")

    def save(self):
        with open(self.CACHE_FILE, "w") as f:
            json.dump({key:getattr(self, key) for key in self.dynamic_keys}, f, indent=4)

    def setup(self):
        if os.path.exists(self.CACHE_FILE):
            self.load()
        else:
            self.save()

    def __repr__(self):
        sb = ["Config:"]
        for key in self.__dict__:
            val = self.__dict__[key]
            sb.append(f"   {key} = {val}")
        return "\n".join(sb)


class Actions:
    def __init__(self, app):
        self.app = app
        self.cfg : Config = app.cfg

    def run(self, cmd, **kwargs):
        if not hasattr(self, cmd):
            return False

        getattr(self, cmd)(argparse.Namespace(**kwargs))
        return True

    def config(self, args : argparse.Namespace):

        if args.key is None and args.value is None:
            print(self.cfg)
            return

        if args.value is None:
            print(getattr(self.cfg, args.key))
            return
        
        if args.key not in self.cfg.dynamic_keys:
            print(f"Unsupport config name {args.key}")
            return

        setattr(self.cfg, args.key, args.value)
        self.cfg.save()
        print("Success!")

    def auth(self, args : argparse.Namespace):
        setattr(self.cfg, "ACCESS_TOKEN", args.token)
        self.cfg.save()
        print("Success!")

    def __run_py(self, file, args):
        code_dir = os.path.realpath(os.path.dirname(file))
        temp_code_file = os.path.join(code_dir, "___tempcode.py")
        shutil.copyfile(file, temp_code_file)
        sys.path.insert(0, code_dir)

        m = __import__("___tempcode", globals(), locals(), ["*"])
        os.remove(temp_code_file)
        getattr(m, "run")(self.app, args)

    def __run_bash(self, file):
        code_dir = os.path.realpath(os.path.dirname(file))
        temp_code_file = os.path.join(code_dir, "___tempcode.sh")
        shutil.copyfile(file, temp_code_file)
        os.system(f'bash \"{temp_code_file}\"')
        os.remove(temp_code_file)

    def get(self, args : argparse.Namespace):
        repo = args.repo
        owner, proj = repo.split("/")

        file = os.path.join(self.cfg.CODE_DIR, repo + ".zip")
        fileurl = f"{self.cfg.SERVER}/public/repo/zip/{repo}?accessToken={self.cfg.ACCESS_TOKEN}"
        md5url  = f"{self.cfg.SERVER}/public/repo/shortinfo/{repo}?accessToken={self.cfg.ACCESS_TOKEN}"
        if not http.require_file_and_check_md5(fileurl, md5url, file, f"Getting {repo}", args.u)[0]:
            print(f"Failed to get repo {repo}.")
            return -1

        http.extract_zip_to(file, proj, False)

        if not args.disable_run:
            os.chdir(proj)
            auto_config_file = ".kiwi/auto.py"
            if os.path.exists(auto_config_file):
                self.__run_py(auto_config_file, args)

            auto_config_file = ".kiwi/auto.sh"
            if os.path.exists(auto_config_file):
                self.__run_bash(auto_config_file)


    def getd(self, args : argparse.Namespace):
        data = args.data
        owner, dname = data.split("/")

        file = os.path.join(self.cfg.DATA_DIR, data + ".zip")
        fileurl = f"{self.cfg.SERVER}/public/data/download/{data}?accessToken={self.cfg.ACCESS_TOKEN}"
        md5url  = f"{self.cfg.SERVER}/public/data/shortinfo/{data}?accessToken={self.cfg.ACCESS_TOKEN}"
        ok, info = http.require_file_and_check_md5(fileurl, md5url, file, f"Getting {data}", args.u)
        if not ok:
            print(f"Failed to install data {data}.")
            return -1

        if info["type"] == "PythonScript":
            if not args.disable_run:
                self.__run_py(file, args)
            else:
                print(f"Script run denied: {file}")
        elif info["type"] == "BashScript":
            if not args.disable_run:
                self.__run_bash(file)
            else:
                print(f"Script run denied: {file}")
        else:
            http.extract_zip_to(file, dname, False)

    def install(self, args : argparse.Namespace):
        pkg = args.pkg
        owner, dname = pkg.split("/")

        file = os.path.join(self.cfg.PKG_DIR, pkg + ".zip")
        fileurl = f"{self.cfg.SERVER}/public/pkg/download/{pkg}?accessToken={self.cfg.ACCESS_TOKEN}"
        md5url  = f"{self.cfg.SERVER}/public/pkg/shortinfo/{pkg}?accessToken={self.cfg.ACCESS_TOKEN}"
        ok, info = http.require_file_and_check_md5(fileurl, md5url, file, f"Getting {pkg}", args.u)
        if not ok:
            print(f"Failed to install pkg {pkg}.")
            return -1

        if info["type"] == "PythonScript":
            if not args.disable_run:
                self.__run_py(file, args)
            else:
                print(f"Script run denied: {file}")
        elif info["type"] == "BashScript":
            if not args.disable_run:
                self.__run_bash(file)
            else:
                print(f"Script run denied: {file}")
        else:
            install_to = os.path.join(self.cfg.LIB_DIR, dname)
            http.extract_zip_to(file, install_to, False)
            print(f"Install to {install_to}")



class Application:
    def __init__(self):
        self.cfg     = Config()
        self.actions = Actions(self)
        self.setup_env()

    def setup_env(self):
        os.makedirs(self.cfg.CACHE_ROOT, exist_ok=True)

    def run_from_command(self):
        cmd = Cmd(self.actions)
        c = cmd.add_cmd("config", "Configure")
        c.add_argument("key",   nargs="?", type=str, help=f"config name, support: {', '.join(self.cfg.dynamic_keys)}")
        c.add_argument("value", nargs="?", type=str, help="config value")

        c = cmd.add_cmd("get", "Get code from server")
        c.add_argument("repo", type=str, help="repo name")
        c.add_argument("-u", action="store_true", help="force update")
        c.add_argument("-disable-run", action="store_true", help="disable auto run")

        c = cmd.add_cmd("auth", "Set auth ACCESS_TOKEN")
        c.add_argument("token", type=str, help="access token name")

        c = cmd.add_cmd("getd", "Get data from server")
        c.add_argument("data", type=str, help="data name")
        c.add_argument("-u", action="store_true", help="force update")
        c.add_argument("-disable-run", action="store_true", help="disable auto run")

        c = cmd.add_cmd("install", "Install package from server")
        c.add_argument("pkg", type=str, help="pkg name")
        c.add_argument("-u", action="store_true", help="force update")
        c.add_argument("-disable-run", action="store_true", help="disable auto run")
        code = cmd.run()
        if code is None:
            code = 0
        sys.exit(code)
        

if __name__ == "__main__":

    app = Application()
    app.run_from_command()