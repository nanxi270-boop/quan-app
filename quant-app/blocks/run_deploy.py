import subprocess
import os
os.chdir(r'C:\Users\AYCS\Desktop\quant-app')
print("🚀 正在部署到 Vercel...")
print("=" * 50)
# 执行部署命令（非交互模式）
result = subprocess.run(
    ['vercel', '--prod', '--yes'],
    capture_output=True,
    text=True,
    shell=True
)
print(result.stdout)
if result.stderr:
    print("⚠️ 错误信息:", result.stderr)
print("=" * 50)
print("\n✅ 部署完成！")
print("💡 请查看上面的输出，找到类似这样的链接：")
print("   https://quan-app-xxx.vercel.app")