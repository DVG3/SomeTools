import os

#file (.exe) code
Code1 = "code1.exe"  
Code2 = "code2.exe" 

#Testcase Generator Program
TestcaseGenerator = "testcaseGenerator.py"

#Compare count
loopCount = 100

for i in range(loopCount):
    print(f'Testcase {i}:')
    os.system(f'python {TestcaseGenerator}') 
    file1 = os.popen(Code1).read()
    file2 = os.popen(Code2).read()
    print(file1)
    print(file2)
    if (file1 != file2):
        print('Different Ans')
        break