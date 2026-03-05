import subprocess
import time
import os
import sys
print("🚀 实际启动BT黑金绿实验室服务器...")
# 检查必要文件
required_files = [
    ("quant-app-deploy/index.html", "HTML文件"),
    ("simple_server.py", "服务器脚本"),
    ("launch.bat", "启动脚本")
]
all_ok = True
for file_path, desc in required_files:
    if os.path.exists(file_path):
        print(f"✅ {desc}: {file_path}")
    else:
        print(f"❌ {desc}不存在: {file_path}")
        all_ok = False
if not all_ok:
    print("❌ 必要文件缺失，无法启动服务器")
    sys.exit(1)
print("\n🔧 启动服务器进程...")
# 启动服务器（在后台）
try:
    # 使用subprocess启动服务器
    server_process = subprocess.Popen(
        [sys.executable, "simple_server.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        universal_newlines=True
    )
    
    print("⏳ 等待服务器启动（5秒）...")
    time.sleep(5)
    
    # 检查进程状态
    if server_process.poll() is None:
        print("✅ 服务器进程正在运行")
        
        # 尝试连接测试
        import requests
        try:
            response = requests.get('http://localhost:8080', timeout=3)
            if response.status_code == 200:
                print(f"✅ 服务器响应正常: HTTP {response.status_code}")
                
                # 检查内容
                if 'BT 黑金绿实验室' in response.text:
                    print("✅ 页面内容正确")
                    
                    # 检查关键元素
                    checks = [
                        ('今日收益', 'KPI指标'),
                        ('总资产', '资产信息'), 
                        ('多空引擎', '交易引擎'),
                        ('QUANT LAB', '品牌标识')
                    ]
                    
                    print("\n📋 页面内容验证:")
                    for text, desc in checks:
                        if text in response.text:
                            print(f"  ✅ 包含{desc}")
                        else:
                            print(f"  ⚠️  缺少{desc}")
                    
                    print(f"\n📊 页面大小: {len(response.text)} 字符")
                    print(f"🌐 访问地址: http://localhost:8080")
                    
                    # 保存状态
                    utils.set_state(
                        success=True,
                        server_running=True,
                        pid=server_process.pid,
                        port=8080,
                        url="http://localhost:8080",
                        html_size=len(response.text),
                        message="✅ 服务器成功启动并运行正常"
                    )
                    
                    print("\n🎉 BT黑金绿实验室已成功部署并运行！")
                    print("💡 服务器将继续在后台运行")
                    print("🛑 要停止服务器，请关闭命令行窗口或按Ctrl+C")
                    
                else:
                    print("❌ 页面内容不正确")
            else:
                print(f"❌ 服务器响应异常: HTTP {response.status_code}")
                
        except requests.ConnectionError:
            print("❌ 无法连接到服务器，可能启动失败")
        except Exception as e:
            print(f"❌ 测试连接时出错: {e}")
            
    else:
        # 获取错误输出
        stdout, stderr = server_process.communicate()
        print("❌ 服务器进程已退出")
        if stdout:
            print(f"标准输出: {stdout}")
        if stderr:
            print(f"错误输出: {stderr}")
            
except Exception as e:
    print(f"❌ 启动服务器时出错: {e}")
print("\n📋 文件位置总结:")
print(f"  1. HTML文件: {os.path.abspath('quant-app-deploy/index.html')}")
print(f"  2. 服务器脚本: {os.path.abspath('simple_server.py')}")
print(f"  3. 启动脚本: {os.path.abspath('launch.bat')}")
print(f"  4. 工作目录: {os.getcwd()}")
print("\n🚀 手动启动方式:")
print("  方法1: 双击 launch.bat")
print("  方法2: 运行 python simple_server.py")
print("  方法3: 运行 python -m http.server 8080 --directory quant-app-deploy")