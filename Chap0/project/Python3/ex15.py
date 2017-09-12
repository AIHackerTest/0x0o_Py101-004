from sys import argv # 从命令行获得参数
script, filename = argv # 提取参数

txt = open(filename) # 根据用户输入打开txt
print(f"Here's your file {filename}:") ## 输出文件名
print(txt.read()) # 输出txt内容
txt.close() 

print("Type the filename again:")
file_again = input(">") #保存用户输入的文件名

txt_again = open(file_again) # 根据文件名打开文件
print(txt_again.read()) # 读文件


