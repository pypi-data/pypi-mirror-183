import argparse

import sys
import os
import yaml
import shutil
from importlib import import_module



class Cli:
    def __init__(self, config_file) -> None:
        self.parser = argparse.ArgumentParser()
        self.config_file = config_file
        
        self.__initialized = False
        if not os.path.exists(self.config_file):
            print(f"Config file: {config_file} not found" )
            return 
            
        with open(self.config_file, 'r') as cf:
            self.cfg = yaml.safe_load(cf.read())
        
        os.makedirs(".tmp", exist_ok=True)
        # self.initialize_envs(self.cfg)
        self.__initialized = True
           
    def initialize_envs(self, env_func_list):
        for arg in env_func_list:
            for k,v in arg.items():
                # print("env", k)
                if os.environ.get(k, None) is not None:
                    continue
                
                with open(f".tmp/{k}.py", 'w') as f:
                    f.write(v)
                m = import_module(k)
                m.execute()

    def __parser_routine(self, cfg, parent, parser, envs):
        self.add_args(parser, cfg.get("args", []))
        self.add_endpoint(parser, parent, cfg.get("entrypoint", None))
        parser.set_defaults(_envs=envs + cfg.get("required_envs", []))
        envs
        sub_parsers = cfg.get("subparsers", None)
        
        if sub_parsers is not None:
            sp = parser.add_subparsers(title=parent)

            for k, v in sub_parsers.items():
                self.__parser_routine(v, f"{parent}.{k}", sp.add_parser(k), envs + cfg.get("required_envs", []))
            
    def add_args(self, parser, args):
        for arg in args:
            if arg["kwargs"].get("type"):
                arg["kwargs"]["type"] = eval(arg["kwargs"]["type"])
                
            parser.add_argument(*arg["list_args"], **arg["kwargs"])
    
    def execute_yml(self, args):
        entrypoint = args._entrypoint
        
        if args._envs is not None:
            self.initialize_envs(args._envs)
        
        m = import_module(entrypoint)
        m.execute(args)
            
            
    def get_sub_cmd(self, args):
        args._sub_parser.print_help()
        return
        
    def add_endpoint(self, parser, parent, cfg_args):
        parser.set_defaults(_sub_parser_name=parent)
        parser.set_defaults(_sub_parser=parser)
        if cfg_args:
            
            mn = parent.replace('.', '_')
            fn = f".tmp/{parent.replace('.', '_')}.py"
            
            with open(fn, 'w') as pyf:
                pyf.write(cfg_args)
            parser.set_defaults(_entrypoint=mn)
            parser.set_defaults(func=self.execute_yml)
        else:
            parser.set_defaults(func=self.get_sub_cmd)
        
    
    def run(self):
        if not self.__initialized:
            return
            
        self.__parser_routine(self.cfg["cli"], "root", self.parser, [])
        args = self.parser.parse_args()
        self.execute_func(args)
        pass
        
    def execute_func(self, args):
        func = getattr(args, "func", lambda *x: self.parser.print_help())
        func(args)
    
    @staticmethod
    def cleanup():
        shutil.rmtree(".tmp")
