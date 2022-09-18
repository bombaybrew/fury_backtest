from backtest.backtest import Backtest

engine = Backtest()
engine.init_data('CDSL.NS')
engine.run()
