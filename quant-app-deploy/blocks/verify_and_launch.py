import os
import subprocess
import time
import sys
import threading
print("🔍 验证部署并启动服务器...")
# 检查当前目录
current_dir = os.getcwd()
print(f"当前目录: {current_dir}")
# 检查必要文件
required_files = [
    ("quant-app-deploy/index.html", "HTML主页面"),
    ("bt_quant_server.py", "服务器脚本"),
    ("启动服务器.bat", "启动脚本"),
    ("使用说明.txt", "使用说明")
]
print("📋 检查文件完整性:")
all_files_exist = True
for file_path, desc in required_files:
    full_path = os.path.join(current_dir, file_path)
    if os.path.exists(full_path):
        size = os.path.getsize(full_path)
        print(f"  ✅ {desc}: {file_path} ({size} 字节)")
    else:
        print(f"  ❌ {desc}不存在: {file_path}")
        all_files_exist = False
if not all_files_exist:
    print("❌ 必要文件缺失，无法启动")
    sys.exit(1)
print("\n✅ 所有必要文件都存在")
# 检查HTML内容
html_path = os.path.join(current_dir, "quant-app-deploy", "index.html")
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()
print(f"📄 HTML内容检查:")
print(f"  文件大小: {len(html_content)} 字符")
# 检查关键内容
key_elements = [
    ("BT 黑金绿实验室", "页面标题"),
    ("今日收益", "KPI指标"),
    ("总资产", "资产信息"),
    ("多空引擎", "交易引擎"),
    ("QUANT LAB", "品牌标识"),
    ("⚡", "闪电图标")
]
all_elements_present = True
for element, desc in key_elements:
    if element in html_content:
        print(f"  ✅ 包含{desc}")
    else:
        print(f"  ❌ 缺少{desc}")
        all_elements_present = False
if not all_elements_present:
    print("⚠️  HTML内容不完整")
else:
    print("✅ HTML内容完整")
# 启动服务器的函数
def start_server():
    """启动服务器"""
    print("\n🚀 启动服务器...")
    try:
        # 使用subprocess启动服务器
        process = subprocess.Popen(
            [sys.executable, "bt_quant_server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1,
            universal_newlines=True
        )
        
        print(f"✅ 服务器进程已启动 (PID: {process.pid})")
        print("⏳ 等待服务器初始化...")
        
        # 等待服务器启动
        time.sleep(3)
        
        # 检查进程状态
        if process.poll() is None:
            print("✅ 服务器正在运行")
            return process
        else:
            stdout, stderr = process.communicate()
            print("❌ 服务器进程已退出")
            if stdout:
                print(f"标准输出: {stdout[:200]}...")
            if stderr:
                print(f"错误输出: {stderr[:200]}...")
            return None
            
    except Exception as e:
        print(f"❌ 启动服务器失败: {e}")
        return None
# 测试连接的函数
def test_connection():
    """测试服务器连接"""
    print("\n🔗 测试服务器连接...")
    try:
        import requests
        response = requests.get('http://localhost:8080', timeout=5)
        if response.status_code == 200:
            print(f"✅ 连接成功: HTTP {response.status_code}")
            
            # 检查响应内容
            if 'BT 黑金绿实验室' in response.text:
                print("✅ 页面内容正确")
                print(f"📊 响应大小: {len(response.text)} 字符")
                
                # 简单内容验证
                content_checks = [
                    ('今日收益', '收益信息'),
                    ('多空引擎', '引擎状态'),
                    ('跟单用户', '用户数据'),
                    ('存入资本', '功能按钮')
                ]
                
                print("  内容验证:")
                for text, desc in content_checks:
                    if text in response.text:
                        print(f"    ✅ {desc}")
                    else:
                        print(f"    ⚠️  {desc}")
                
                return True
            else:
                print("❌ 页面内容不正确")
                return False
        else:
            print(f"❌ 连接失败: HTTP {response.status_code}")
            return False
            
    except requests.ConnectionError:
        print("❌ 无法连接到服务器")
        return False
    except Exception as e:
        print(f"❌ 测试过程中出错: {e}")
        return False
# 主执行流程
print("\n" + "="*60)
print("        BT黑金绿实验室 - 部署验证测试")
print("="*60)
# 启动服务器
server_process = start_server()
if server_process:
    # 测试连接
    if test_connection():
        print("\n🎉 恭喜！部署验证通过！")
        print("\n📋 部署总结:")
        print(f"  工作目录: {current_dir}")
        print(f"  HTML文件: quant-app-deploy/index.html")
        print(f"  服务器脚本: bt_quant_server.py")
        print(f"  启动脚本: 启动服务器.bat")
        print(f"  访问地址: http://localhost:8080")
        print(f"  服务器PID: {server_process.pid}")
        
        # 设置成功状态
        utils.set_state(
            success=True,
            deployed=True,
            server_running=True,
            pid=server_process.pid,
            port=8080,
            url="http://localhost:8080",
            html_file=html_path,
            server_script="bt_quant_server.py",
            launch_script="启动服务器.bat",
            message="✅ BT黑金绿实验室成功部署并运行！"
        )
        
        print("\n🚀 使用说明:")
        print("  1. 服务器已在后台运行")
        print("  2. 浏览器访问: http://localhost:8080")
        print("  3. 双击'启动服务器.bat'可重新启动")
        print("  4. 按Ctrl+C停止当前服务器")
        print("\n💡 提示: 查看'使用说明.txt'获取详细信息")
        
    else:
        print("\n❌ 服务器连接测试失败")
        # 停止服务器进程
        if server_process.poll() is None:
            server_process.terminate()
            print("🛑 已停止服务器进程")
        
        utils.set_state(success=False, error="服务器连接测试失败")
else:
    print("\n❌ 服务器启动失败")
    utils.set_state(success=False, error="服务器启动失败")
print("\n" + "="*60)