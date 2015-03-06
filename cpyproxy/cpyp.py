import sys
import pyslave
import inspect
import os
cpyp_slave = pyslave.pyslave()
FAKE_MODULE_NAME = 'cpyp'

class PathLoader(object):
    def __init__(self, importerpath, path):
        self.importerpath = importerpath
        self.path = path
    
    def __get_module(self, name):
        if name == FAKE_MODULE_NAME:
            return cpyp_slave
        
        modname = name[len(FAKE_MODULE_NAME)+1:]
        # Hack the calling module path to the remote sys.path
        # so we can load (implicit) relative stuff. Couldn't
        # get remote imp.find_module working :(
        cpyp_slave.modules.sys.path.insert(0, self.importerpath)
        try:
            return cpyp_slave.modules[modname]
        finally:
            cpyp_slave.modules.sys.path.pop(0)

    def load_module(self, name):
        mod = self.__get_module(name)
        sys.modules[name] = mod
        return mod

class _ImportHack:
    def _is_my_module(self, name):
        return name == FAKE_MODULE_NAME or name.startswith(FAKE_MODULE_NAME+".")
    
    def find_module(self, name, path):
        if self._is_my_module(name):
            localpath = os.path.dirname(os.path.abspath(inspect.stack()[1][1]))
            return PathLoader(localpath, path)
    
    def __nonzero__(self):
            return True
    
    def __path__(self): return None



sys.meta_path.append(_ImportHack())
