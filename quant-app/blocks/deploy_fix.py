import subprocess
import os
os.chdir(r'C:\Users\AYCS\Desktop\quant-app')
print("🚀 正在部署到 Vercel...")
print("=" * 50)
# 使用 UTF-8 编码执行部署
result = subprocess.run(
    'vercel --prod --yes',
    capture_output=True,
    text=True,
    encoding='utf-8',
    errors='ignore',
    shell=True
)
print(result.stdout)
if result.stderr:
    print("⚠️ 输出信息:", result.stderr)
print("=" * 50)
print("\n✅ 部署命令已执行！")
print("💡 如果部署成功，链接会显示在上面")