import sys

if __name__=="__main__":
    ver = sys.argv[1]
    f = open("C:\\Source\\PROJECT_NAME\\PROJECT_NAME\\Source\\PROJECT_NAME\\public\\PROJECT_NAME.h")
    lines = [line.rstrip('\n') for line in f]
    f.close()
    f = open(ver, 'w')
    for line in lines:
        if("PROJECT_NAME_BUILD_NUMBER" in line):
            line = "#define FOG_BUILD_NUMBER " + str(ver)
        f.write(line)
    f.close()
