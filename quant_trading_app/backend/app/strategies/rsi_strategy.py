"""
RSI相对强弱指数策略
"""
import pandas as pd
import numpy as np
class RSIStrategy:
    def __init__(self, rsi_period=14, oversold=30, overbought=70):
        self.rsi_period = rsi_period
        self.oversold = oversold
        self.overbought = overbought
        
    def calculate_rsi(self, prices: pd.Series) -> pd.Series:
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=self.rsi_period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=self.rsi_period).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
        
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['RSI'] = self.calculate_rsi(df['Close'])
        df['signal'] = 0
        # RSI低于超卖线买入
        df.loc[df['RSI'] < self.oversold, 'signal'] = 1
        # RSI高于超买线卖出
        df.loc[df['RSI'] > self.overbought, 'signal'] = -1
        return df
