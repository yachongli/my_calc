import sys
import psutil
import os
def main(who):
    kill_list = []
    pids = psutil.pids()
    try:
        for pid in pids:
            process = psutil.Process(pid)
            cmd_list = process.cmdline()
            for cmd in cmd_list:
                if "%s.py"% who in cmd.split("/"):
                    kill_list.append(pid)
                    print cmd_list
    except:
        pass
    print kill_list
    for kill in kill_list:
        os.kill(kill,9)


if __name__ == "__main__":
    main(sys.argv[1])