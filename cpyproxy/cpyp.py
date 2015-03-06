import sys
import pyslave
cpyp_slave = pyslave.pyslave()
FAKE_MODULE_NAME = 'cpyp'

class _ImportHack:
    def _is_my_module(self, name):
        return name == FAKE_MODULE_NAME or name.startswith(FAKE_MODULE_NAME+".")
    
    def find_module(self, name, path):
        if self._is_my_module(name):
            return self
    
    def __nonzero__(self):
            return True
    
    def __path__(self): return None

    def load_module(self, name):
        assert self._is_my_module(name)
        if name == FAKE_MODULE_NAME:
            mod = cpyp_slave
        else:
            modname = name[len(FAKE_MODULE_NAME)+1:]
            mod = cpyp_slave.modules[modname]
        sys.modules[name] = mod
        return mod


sys.meta_path.append(_ImportHack())
