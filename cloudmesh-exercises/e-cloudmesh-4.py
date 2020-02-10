# sp20-516-233 E.Cloudmesh.Common.4

# Develop a program that demonstrates the use of cloudmesh.common.Shell
from cloudmesh.common.Shell import Shell

if __name__ == "__main__":
    # this is the command for getting the path but still gives errors
    # result = Shell.execute('echo %cd%')

    print("These commands are for Windows 10 EDU")
    r1 = Shell.check_python()
    print(r1)
    r2 = Shell.pip()
    print(r2)
    r3 = Shell.ls()
    print(r3)
    # the following code gives UNDEFINED_TERMINAL_TYPE
    r4 = Shell.terminal_type()
    print(r4)
    # the following code gives win32 but I'm on a 64 bit system
    r5 = Shell.operating_system()
    print(r5)

    # commands below do not work
    # result = Shell.execute('pwd')
    # print(result)
    # result = Shell.execute('ls', ["-l", "-a"])
    # print(result)
    # result = Shell.execute('ls', "-l -a")
    # print(result)
