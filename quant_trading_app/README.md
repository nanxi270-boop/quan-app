# 量化交易应用 - 完整源码部署
## 项目简介
这是一个完整的量化交易应用，包含：
- 后端Python FastAPI服务
- 前端Vue.js量化交易界面
- 多种量化交易策略
- 回测功能
- 实盘监控
## 快速开始
### 1. 环境要求
- Python 3.9+
- Node.js 16+
- pip / npm
### 2. 后端安装
```bash
cd backend
pip install -r ../requirements.txt
python main.py
```
服务将在 http://localhost:8000 启动
### 3. 前端安装
```bash
cd frontend
npm install
npm run dev
```
前端将在 http://localhost:5173 启动
### 4. 使用Docker部署（可选）
```bash
docker-compose up -d
```
## 功能特性
✅ 多种量化策略（均线、RSI、MACD、布林带）
✅ 历史数据回测
✅ 实时行情监控
✅ 资产组合管理
✅ 风险控制
✅ RESTful API
## 策略列表
1. **均线交叉策略** - 基于SMA5/SMA20交叉信号
2. **RSI策略** - 超买超卖反转策略
3. **布林带策略** - 均值回归策略
4. **MACD策略** - 趋势跟踪策略
## 项目结构
```
quant_trading_app/
├── backend/             # 后端Python代码
│   ├── main.py         # 主程序入口
│   ├── app/
│   │   ├── api/        # API路由
│   │   ├── core/       # 核心配置
│   │   ├── models/     # 数据模型
│   │   ├── services/   # 业务服务
│   │   └── strategies/ # 策略实现
├── frontend/           # 前端Vue代码
├── docs/              # 文档
└── requirements.txt   # Python依赖
```
## 许可证
MIT License
