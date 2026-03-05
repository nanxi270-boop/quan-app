import subprocess
import os
os.chdir(r'C:\Users\AYCS\Desktop\quant-app')
print("🔐 正在打开 Vercel 登录...")
print("=" * 50)
# 打开登录页面
subprocess.Popen(['vercel', 'login'], shell=True)
print("\n📋 登录步骤：")
print("1. 浏览器会自动打开 Vercel 登录页面")
print("2. 使用您的账号登录")
print("3. 登录成功后，告诉我，我再帮您部署")
print("=" * 50)