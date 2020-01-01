filename = input()
filename1 = input()
filename2 = input()

fileexten = filename.split('.')
fileexten1 = filename1.split('.')
fileexten2 = filename2.split('.')

print('The extension of the file is : ' + fileexten[-1])
print('The extension of the file is : ' + fileexten1[-1])
print('The extension of the file is : ' + fileexten2[-1])