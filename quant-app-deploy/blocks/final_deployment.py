import os
import sys
import time
print("🎯 最终部署 - 从正确位置创建所有文件")
# 获取正确的工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")
print(f"目录内容: {os.listdir(current_dir)}")
# 检查是否在正确的目录
if "quant-app-deploy" in current_dir:
    # 如果已经在部署目录内，退回到上级目录
    os.chdir("..")
    current_dir = os.getcwd()
    print(f"切换到上级目录: {current_dir}")
# 创建部署目录
deploy_dir = os.path.join(current_dir, "quant-app-deploy")
os.makedirs(deploy_dir, exist_ok=True)
print(f"✅ 部署目录: {deploy_dir}")
# 创建HTML文件
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
html_file = os.path.join(deploy_dir, "index.html")
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html_content)
print(f"✅ 创建HTML文件: {html_file} ({os.path.getsize(html_file)} 字节)")
# 创建简化的服务器脚本
server_script = os.path.join(current_dir, "bt_quant_server.py")
server_code = '''import http.server
import socketserver
import os
import webbrowser
import time
PORT = 8080
class BTQuantHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/', '/index.html', '/index.htm']:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            self.end_headers()
            
            html_path = os.path.join(os.path.dirname(__file__), 'quant-app-deploy', 'index.html')
            try:
                with open(html_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                self.wfile.write(content.encode('utf-8'))
                print(f"[{time.strftime('%H:%M:%S')}] ✅ 服务HTML页面 ({len(content)} 字节)")
            except Exception as e:
                self.wfile.write(f'<h1>500 - Server Error</h1><p>{e}</p>'.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - Not Found')
print("=" * 60)
print("       BT黑金绿实验室 - 量化交易面板服务器")
print("=" * 60)
print()
print(f"📁 服务目录: {os.path.join(os.getcwd(), 'quant-app-deploy')}")
print(f"📄 HTML文件: index.html")
print(f"🌐 访问地址: http://localhost:{PORT}")
print()
try:
    with socketserver.TCPServer(("", PORT), BTQuantHandler) as httpd:
        print(f"✅ 服务器已在端口 {PORT} 启动")
        print(f"⏰ 启动时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"💡 按 Ctrl+C 停止服务器")
        print("-" * 60)
        
        # 打开浏览器
        webbrowser.open(f'http://localhost:{PORT}')
        
        # 启动服务器
        httpd.serve_forever()
        
except OSError as e:
    if "Address already in use" in str(e) or "10048" in str(e):
        print(f"❌ 端口 {PORT} 被占用，请尝试:")
        print(f"   1. 关闭其他使用端口 {PORT} 的程序")
        print(f"   2. 或修改脚本中的 PORT 变量为其他端口（如 8081, 8088）")
    else:
        print(f"❌ 启动失败: {e}")
except KeyboardInterrupt:
    print("\\n🛑 服务器已停止")
except Exception as e:
    print(f"❌ 服务器错误: {e}")
'''
with open(server_script, 'w', encoding='utf-8') as f:
    f.write(server_code)
print(f"✅ 创建服务器脚本: {server_script}")
# 创建Windows启动脚本
bat_script = os.path.join(current_dir, "启动服务器.bat")
bat_content = '''@echo off
chcp 65001 >nul
echo ========================================
echo    BT黑金绿实验室 - 一键启动服务器
echo ========================================
echo.
echo 正在启动量化交易面板服务器...
echo.
cd /d "%~dp0"
if exist "bt_quant_server.py" (
    echo ✅ 找到服务器脚本
    echo 🚀 启动服务器中...
    echo 🌐 访问地址: http://localhost:8080
    echo.
    python bt_quant_server.py
) else (
    echo ❌ 错误: 服务器脚本 bt_quant_server.py 不存在
    echo.
    pause
)
'''
with open(bat_script, 'w', encoding='utf-8') as f:
    f.write(bat_content)
print(f"✅ 创建启动脚本: {bat_script}")
# 创建使用说明
readme_file = os.path.join(current_dir, "使用说明.txt")
readme_content = f'''BT黑金绿实验室 - 量化交易面板
部署完成时间: {time.strftime('%Y-%m-%d %H:%M:%S')}
📁 文件结构:
{current_dir}/
├── quant-app-deploy/      # 部署目录
│   └── index.html        # 主页面文件
├── bt_quant_server.py    # 服务器脚本
├── 启动服务器.bat        # 一键启动脚本
└── 使用说明.txt          # 本文件
🚀 启动方式（任选其一）:
1. 【最简单】双击 "启动服务器.bat"
2. 【命令行】运行: python bt_quant_server.py
3. 【备用】运行: python -m http.server 8080 --directory quant-app-deploy
🌐 访问地址:
- 本地访问: http://localhost:8080
- 局域网访问: http://[你的IP地址]:8080
🔧 技术信息:
- 服务器端口: 8080
- 页面编码: UTF-8
- 文件大小: {os.path.getsize(html_file)} 字节
- 支持缓存控制: 无缓存
⚠️ 注意事项:
1. 确保Python 3.6+环境
2. 如果端口8080被占用，修改bt_quant_server.py中的PORT变量
3. 按Ctrl+C停止服务器
4. 防火墙可能需要允许端口8080
📞 验证方式:
1. 启动服务器后，浏览器访问 http://localhost:8080
2. 应看到"BT黑金绿实验室"黑色金色主题页面
3. 包含KPI指标、多空引擎状态等信息
祝您使用愉快！
BT黑金绿实验室 · 24/7量化交易系统
'''
with open(readme_file, 'w', encoding='utf-8') as f:
    f.write(readme_content)
print(f"✅ 创建使用说明: {readme_file}")
# 验证文件
print("\n📋 文件清单验证:")
files_to_check = [
    (html_file, "HTML文件"),
    (server_script, "服务器脚本"),
    (bat_script, "启动脚本"),
    (readme_file, "使用说明")
]
all_ok = True
for file_path, desc in files_to_check:
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"  ✅ {desc}: {os.path.basename(file_path)} ({size} 字节)")
    else:
        print(f"  ❌ {desc}不存在")
        all_ok = False
if all_ok:
    print("\n🎉 所有文件创建成功！")
    # 设置成功状态
    utils.set_state(
        success=True,
        html_file=html_file,
        server_script=server_script,
        launch_script=bat_script,
        readme_file=readme_file,
        deploy_dir=deploy_dir,
        port=8080,
        url="http://localhost:8080",
        message="✅ BT黑金绿实验室部署完成！"
    )
    
    print("\n🚀 部署完成！下一步:")
    print(f"  1. 双击 '{os.path.basename(bat_script)}' 启动服务器")
    print(f"  2. 浏览器访问: http://localhost:8080")
    print(f"  3. 查看 '{os.path.basename(readme_file)}' 获取详细信息")
else:
    print("\n❌ 部分文件创建失败")
    utils.set_state(success=False, error="文件创建失败")