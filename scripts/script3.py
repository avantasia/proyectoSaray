import subprocess

class Script3:
    def funcion1(self) -> str:
        result = subprocess.run(['dir','/A'], shell=True,stdout=subprocess.PIPE,universal_newlines=True )
        return result.stdout
