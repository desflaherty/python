#f = open('newfile.txt','w') this is write 'a' is append
f = open('newfile.txt','a')
lines = ['hello','world','welcome','to','file IO']
text ='\n'.join(lines)
f.writelines(text)
f.close()
