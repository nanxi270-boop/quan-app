"""
均线交叉策略
"""
import pandas as pd
import numpy as np
class MAStrategy:
    def __init__(self, short_window=5, long_window=20):
        self.short_window = short_window
        self.long_window = long_window
        
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        df = data.copy()
        df['SMA_SHORT'] = df['Close'].rolling(self.short_window).mean()
        df['SMA_LONG'] = df['Close'].rolling(self.long_window).mean()
        df['signal'] = 0
        # 金叉买入
        df.loc[df['SMA_SHORT'] > df['SMA_LONG'], 'signal'] = 1
        # 死叉卖出
        df.loc[df['SMA_SHORT'] < df['SMA_LONG'], 'signal'] = -1
        return df
