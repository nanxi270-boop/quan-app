"""
量化交易应用 - 后端主程序
"""
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
app = FastAPI(title="量化交易API", version="1.0.0")
# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 数据模型
class StrategyConfig(BaseModel):
    name: str
    symbols: List[str]
    parameters: Dict
    enabled: bool = True
class BacktestRequest(BaseModel):
    symbol: str
    start_date: str
    end_date: str
    strategy: str
    initial_capital: float = 100000.0
# API路由
@app.get("/")
async def root():
    return {"status": "ok", "message": "量化交易API运行正常", "version": "1.0.0"}
@app.get("/api/market/data/{symbol}")
async def get_market_data(symbol: str, period: str = "1y"):
    """获取市场数据"""
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period)
        data = hist.reset_index().to_dict('records')
        return {"symbol": symbol, "data": data}
    except Exception as e:
        logger.error(f"获取市场数据失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/api/backtest")
async def run_backtest(request: BacktestRequest):
    """运行回测"""
    try:
        # 获取数据
        ticker = yf.Ticker(request.symbol)
        data = ticker.history(start=request.start_date, end=request.end_date)
        
        # 简单均线策略回测
        result = simple_ma_strategy(data, request.initial_capital)
        return result
    except Exception as e:
        logger.error(f"回测失败: {e}")
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/api/strategies")
async def get_strategies():
    """获取可用策略列表"""
    strategies = [
        {"id": "ma_cross", "name": "均线交叉策略", "description": "简单移动平均线交叉策略"},
        {"id": "rsi", "name": "RSI策略", "description": "相对强弱指数反转策略"},
        {"id": "bollinger", "name": "布林带策略", "description": "布林带均值回归策略"},
        {"id": "macd", "name": "MACD策略", "description": "MACD指标交易策略"}
    ]
    return {"strategies": strategies}
@app.get("/api/account/info")
async def get_account_info():
    """获取账户信息"""
    return {
        "balance": 125680.50,
        "total_profit": 15680.50,
        "daily_pnl": 342.80,
        "positions": [
            {"symbol": "AAPL", "quantity": 100, "avg_price": 175.50, "current_price": 182.30, "pnl": 680.00},
            {"symbol": "MSFT", "quantity": 50, "avg_price": 380.20, "current_price": 395.10, "pnl": 745.00},
            {"symbol": "GOOGL", "quantity": 30, "avg_price": 140.80, "current_price": 142.60, "pnl": 54.00}
        ]
    }
def simple_ma_strategy(data: pd.DataFrame, initial_capital: float):
    """简单均线策略实现"""
    data['SMA5'] = data['Close'].rolling(5).mean()
    data['SMA20'] = data['Close'].rolling(20).mean()
    
    position = 0
    capital = initial_capital
    shares = 0
    trades = []
    equity_curve = []
    
    for idx, row in data.iterrows():
        if pd.isna(row['SMA5']) or pd.isna(row['SMA20']):
            continue
            
        # 金叉买入
        if row['SMA5'] > row['SMA20'] and position == 0:
            shares = int(capital / row['Close'])
            cost = shares * row['Close']
            capital -= cost
            position = 1
            trades.append({
                "date": idx.strftime("%Y-%m-%d"),
                "type": "buy",
                "price": row['Close'],
                "shares": shares
            })
        
        # 死叉卖出
        elif row['SMA5'] < row['SMA20'] and position == 1:
            revenue = shares * row['Close']
            capital += revenue
            position = 0
            trades.append({
                "date": idx.strftime("%Y-%m-%d"),
                "type": "sell",
                "price": row['Close'],
                "shares": shares
            })
        
        # 计算当前权益
        current_equity = capital + (position * shares * row['Close'])
        equity_curve.append({
            "date": idx.strftime("%Y-%m-%d"),
            "equity": current_equity
        })
    
    # 计算最终结果
    final_price = data['Close'].iloc[-1]
    final_equity = capital + (position * shares * final_price)
    total_return = (final_equity - initial_capital) / initial_capital * 100
    
    return {
        "initial_capital": initial_capital,
        "final_equity": final_equity,
        "total_return_pct": total_return,
        "num_trades": len(trades),
        "trades": trades,
        "equity_curve": equity_curve
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
