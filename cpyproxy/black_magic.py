import sys
import imp
import pyslave
cpyp_slave = pyslave.pyslave()

# This could break badly on multithreading, but
# I have a hunch that GIL is in effect for the whole
# import process, so going lazy with locks here.
class _ImportHack:
    def __init__(self, slave):
        self._ignore_me = False
        self.slave = slave

    def _has_system_module(self, name, path):
        self._ignore_me = True
        try:
            imp.find_module(name, path)
        except ImportError:
            return False
        finally:
            self._ignore_me = False
        return True
        return system_mod
    
    def find_module(self, name, path):
        if self._ignore_me: return None
        if self._has_system_module(name, path): return None
        return self
    
    def load_module(self, name):
        mod = self.slave.modules[name]
        sys.modules[name] = mod
        return mod

sys.meta_path.append(_ImportHack(cpyp_slave))

if __name__ == '__main__':
    # We are being run as a script or with -m flag,
    # so execute whatever we have left in argv
    myargs = sys.argv[1:]
    __package__ = ''
    if len(myargs) > 0:
        execfile(myargs[0])
    else:
        import code
        code.interact()
