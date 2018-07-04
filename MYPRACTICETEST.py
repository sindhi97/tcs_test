def ghgh(site_name):
    print("HEYYYYY")

def printMessage(ghgh):

    # print("Hello")
    def nestedFN(site_name):
        return "Yash " + ghgh(site_name)

    return nestedFN

@printMessage
def site(site_name) :
    return site_name

print(site("google.com"))




# stir = "             The quick brown fox jumped over the fence               "
# stir = stir.strip()
#
# print(stir, "Yash")
# import re
# inputString = "contact us at: support@datacmp.com"
# match = re.search(r'([\w]*)@(\w+)\.(\w+)',inputString)
# if match:
#     print(match.group(1))

# sti = "b####b###bb###3"
# for i in range(len(sti)):
#     if sti[i] == 'b':
#         print(i)
#




# lstA = [2,3,4,5,6,7,8]
# lstB = [10,12]
# if set(lstA).intersection(lstB) :
#     print(set(lstA).intersection(lstB))
# else :
#     print("No value found")

import os
# print(os.path)
# print(os.getcwd())
# print(os.path.abspath('.'))
# print(os.listdir('.'))
#
# file = open("testfile","w")
#
# file.write("Hello Writing in file\n")
# file.write("New line in the same file\n")
# file.write("Next step is to close the file\n")
#
# file.close()
#
#
# f = open("testfileee","r")
# print(f.read())
# f.close()


