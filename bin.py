import sys,subprocess;from time import sleep

if sys.platform=="win32" or sys.platform=="win64":
 subprocess.call("cls")
else:
 subprocess.call("clear")
 
banner = """
 (*) Author   : X14N23N6
 (*) Team     : Blackhole Security
 (*) Purpose  : Encode and Decode Binary
 (*) Version  : 1
"""
print banner


def encode():
 while True:
  try:
   string = str(raw_input("(*) String>> "))
   print "(*) Binary : "
   pro = " ".join(format(ord(x),"b") for x in string)
   print pro
  except:
   exit()
 
if __name__ == "__main__":
 encode()