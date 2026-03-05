import os
import shutil
import sys
import time
print("🔧 修复部署问题并启动服务器...")
# 获取当前目录
current_dir = os.getcwd()
print(f"当前目录: {current_dir}")
# 检查并修复文件位置问题
deploy_dir = os.path.join(current_dir, "quant-app-deploy")
if not os.path.exists(deploy_dir):
    print(f"❌ 部署目录不存在: {deploy_dir}")
    sys.exit(1)
print(f"✅ 部署目录存在: {deploy_dir}")
# 检查HTML文件
html_file = os.path.join(deploy_dir, "index.html")
if not os.path.exists(html_file):
    print(f"❌ HTML文件不存在: {html_file}")
    # 重新创建HTML文件
    html_content = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BT 黑金绿实验室</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        body {
            background-color: #0A0A0A;
            color: #FFFFFF;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        
        .container {
            max-width: 700px;
            width: 100%;
            background: #0A0A0A;
            border: 1px solid #2C2C2E;
            border-radius: 24px;
            padding: 30px;
        }
        
        h1 {
            color: #FFD700;
            font-size: 36px;
            font-weight: 600;
            letter-spacing: 2px;
            margin-bottom: 8px;
        }
        
        .subtitle {
            color: #8E8E93;
            font-size: 14px;
            margin-bottom: 30px;
            border-bottom: 1px solid #2C2C2E;
            padding-bottom: 20px;
        }
        
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin: 30px 0;
        }
        
        .kpi-card {
            background: #1A1A1A;
            border: 1px solid #2C2C2E;
            border-radius: 16px;
            padding: 20px;
        }
        
        .kpi-label {
            color: #8E8E93;
            font-size: 12px;
            margin-bottom: 8px;
        }
        
        .kpi-value {
            color: #00FFB9;
            font-size: 24px;
            font-weight: 600;
        }
        
        .stat-row {
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid #2C2C2E;
        }
        
        .stat-label {
            color: #8E8E93;
        }
        
        .stat-value {
            color: #00FFB9;
            font-weight: 500;
        }
        
        .ticker {
            background: #1A1A1A;
            border-left: 4px solid #00FFB9;
            border-radius: 16px;
            padding: 20px;
            margin: 25px 0;
        }
        
        .ticker-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            color: #8E8E93;
        }
        
        .ticker-item span:last-child {
            color: #00FFB9;
        }
        
        .action-buttons {
            display: flex;
            gap: 15px;
            margin: 30px 0;
        }
        
        .btn {
            flex: 1;
            background: transparent;
            border: 1px solid #FFD700;
            color: #FFD700;
            padding: 14px 0;
            border-radius: 40px;
            text-align: center;
        }
        
        .bottom-menu {
            display: flex;
            justify-content: space-around;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #2C2C2E;
        }
        
        .menu-item {
            color: #8E8E93;
        }
        
        .menu-item.active {
            color: #FFD700;
        }
        
        .footer {
            text-align: center;
            color: #5C5C5E;
            font-size: 12px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>⚡ BT 黑金绿实验室</h1>
        <div class="subtitle">QUANT LAB · EST. 2024</div>
        
        <div class="kpi-grid">
            <div class="kpi-card"><div class="kpi-label">今日收益</div><div class="kpi-value">+4.87%</div></div>
            <div class="kpi-card"><div class="kpi-label">总资产</div><div class="kpi-value">124.8K</div></div>
            <div class="kpi-card"><div class="kpi-label">跟单用户</div><div class="kpi-value">12.8K</div></div>
            <div class="kpi-card"><div class="kpi-label">策略胜率</div><div class="kpi-value">78.3%</div></div>
        </div>
        
        <div class="stat-row"><span class="stat-label">多空引擎</span><span class="stat-value">ACTIVE · 毫秒级</span></div>
        <div class="stat-row"><span class="stat-label">今日吞吐</span><span class="stat-value">$4.87M +23.4%</span></div>
        <div class="stat-row"><span class="stat-label">跟单用户</span><span class="stat-value">12,847 · 在线 3,284</span></div>
        <div class="stat-row"><span class="stat-label">策略胜率</span><span class="stat-value">78.3% · 夏普 3.92</span></div>
        
        <div class="ticker">
            <div class="ticker-item"><span>用户 ***8</span><span>+1,247U</span></div>
            <div class="ticker-item"><span>用户 ***2</span><span>存入 5,000U</span></div>
            <div class="ticker-item"><span>用户 ***5</span><span>跟单 v4</span></div>
        </div>
        
        <div class="action-buttons">
            <div class="btn">存入资本</div>
            <div class="btn">提取收益</div>
        </div>
        
        <div class="bottom-menu">
            <span class="menu-item">交易</span>
            <span class="menu-item active">量化</span>
            <span class="menu-item">跟单</span>
            <span class="menu-item">资产</span>
        </div>
        
        <div class="footer">BT 黑金绿实验室 · 24/7 运行</div>
    </div>
</body>
</html>'''
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ 已重新创建HTML文件: {html_file}")
print(f"✅ HTML文件: {html_file} ({os.path.getsize(html_file)} 字节)")
# 复制服务器脚本到当前目录
server_scripts = ["quant_server_optimized.py", "start_server.bat", "test_server.py"]
for script in server_scripts:
    src = os.path.join(current_dir, "blocks", script)
    dst = os.path.join(current_dir, script)
    
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"✅ 复制 {script} 到当前目录")
    else:
        print(f"⚠️  源文件不存在: {src}")
# 创建简化的服务器启动脚本
simple_server = os.path.join(current_dir, "simple_server.py")
with open(simple_server, 'w', encoding='utf-8') as f:
    f.write('''import http.server
import socketserver
import os
import webbrowser
import socket
import time
PORT = 8080
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html_path = os.path.join(os.path.dirname(__file__), 'quant-app-deploy', 'index.html')
            with open(html_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.wfile.write(content.encode('utf-8'))
        else:
            super().do_GET()
print("=" * 50)
print("   BT黑金绿实验室 - 服务器启动")
print("=" * 50)
print(f"服务目录: {os.path.join(os.getcwd(), 'quant-app-deploy')}")
print(f"HTML文件: index.html")
# 切换到部署目录
os.chdir('quant-app-deploy')
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"\\n✅ 服务器已启动!")
        print(f"🌐 访问地址: http://localhost:{PORT}")
        print(f"⏰ 启动时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("\\n💡 按 Ctrl+C 停止服务器")
        print("=" * 50)
        
        # 打开浏览器
        webbrowser.open(f'http://localhost:{PORT}')
        
        httpd.serve_forever()
except OSError:
    print(f"❌ 端口 {PORT} 被占用，请关闭其他使用该端口的程序")
except KeyboardInterrupt:
    print("\\n🛑 服务器已停止")
except Exception as e:
    print(f"❌ 启动失败: {e}")
''')
print(f"✅ 创建简化服务器脚本: {simple_server}")
# 创建最终启动脚本
final_bat = os.path.join(current_dir, "launch.bat")
with open(final_bat, 'w', encoding='utf-8') as f:
    f.write('''@echo off
echo ========================================
echo    BT黑金绿实验室 - 一键启动
echo ========================================
echo.
echo 正在启动量化交易面板服务器...
echo.
cd /d "%~dp0"
if exist "simple_server.py" (
    echo ✅ 找到服务器脚本
    echo 🚀 启动服务器中...
    python simple_server.py
) else (
    echo ❌ 服务器脚本不存在
    pause
)
''')
print(f"✅ 创建最终启动脚本: {final_bat}")
# 生成最终状态
utils.set_state(
    success=True,
    html_file=html_file,
    server_script="simple_server.py",
    launch_script="launch.bat",
    deploy_dir=deploy_dir,
    access_url="http://localhost:8080",
    message="✅ 所有文件准备就绪，可以启动服务器"
)
print("\\n🎉 修复完成！文件清单:")
print(f"  1. {html_file}")
print(f"  2. {simple_server}")
print(f"  3. {final_bat}")
print(f"  4. {deploy_dir}/ (部署目录)")
print("\\n🚀 启动方式:")
print("  1. 双击 launch.bat (推荐)")
print("  2. 或运行: python simple_server.py")
print("\\n🌐 访问地址: http://localhost:8080")