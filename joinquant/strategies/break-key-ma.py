# coding:utf-8
# 导入函数库
import jqdata
import pandas as pd

# 初始化函数，设定基准等等
def initialize(context):
    # 设定沪深300作为基准
    set_benchmark('000300.XSHG')
    # 开启动态复权模式(真实价格)
    set_option('use_real_price', True)
    # 输出内容到日志 log.info()
    log.info('初始函数开始运行且全局只运行一次')
    # 过滤掉order系列API产生的比error级别低的log
    log.set_level('order', 'error')
    # log.info(g.stockindex)
    ### 股票相关设定 ###
    # 股票类每笔交易时的手续费是：买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税, 每笔交易佣金最低扣5块钱
    set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
    
    g.con_START_DATE = 150 # 股票上市时间限制
    # 剔除
    g.available_lists = []
    g.bought_lists = []
    
    ## 运行函数（reference_security为运行时间的参考标的；传入的标的只做种类区分，因此传入'000300.XSHG'或'510300.XSHG'是一样的）
    g.security = '002680.XSHE'
    # 参照股指期货的时间每分钟运行一次, 必须选择分钟回测, 否则每天执行
    run_daily(market_open, 'open' ) 
    run_daily(check_stocks, 'every_bar', reference_security='IF1512.CCFX') #选股
    # run_daily(trade, 'every_bar') #交易
   
    
## 开盘前运行函数     
def before_market_open(context):
    # 输出运行时间
    log.info('函数运行时间(before_market_open)：'+str(context.current_dt.time()))

    # 给微信发送消息（添加模拟交易，并绑定微信生效）
    send_message('美好的一天~')

    # 要操作的股票：平安银行（g.为全局变量）
    # g.security = '600874.XSHG'
    
    log.info('before_market_open end')
    
## 开盘时运行函数
def market_open(context):
    log.info('函数运行时间(market_open):'+str(context.current_dt.time()))
    g.available_list =  get_available_stocks(context)
    log.info('available_list: '.format(g.available_list))
    
    
## 收盘后运行函数  
def after_market_close(context):
    log.info(str('函数运行时间(after_market_close):'+str(context.current_dt.time())))
    #得到当天所有成交记录
    trades = get_trades()
    for _trade in trades.values():
        log.info('成交记录：{}'.format(str(_trade)))
    log.info('一天结束')
    log.info('##############################################################')


def get_available_stocks(context):
    '''
    run in before_market_open
    '''
    #将所有股票列表转换成数组
    buy_lists = list(get_all_securities(['stock']).index)
    
    # 过滤停股票
    buy_lists = paused_filter(context, buy_lists)
    # 过滤退市股票
    buy_lists = delisted_filter(context, buy_lists)
    
    return buy_lists


def handle_data(context, data):
    stocks = g.available_list
    stocks = [g.security]
    
    for security in stocks:
        log.warn('current stock: {}'.format(security))
    # 得到股票之前n d/min的moving平均价，不包括现在
    # log.info('lastl {}'.format(data[g.security])
    # MA60 = current_data[g.security].mavg(60)
    # log.info(data[g.security].money)
    # log.info('money10: {}'.format(data[g.security].mavg(10, field='money')))
        arr = get_bars(security, 60, unit='1d',
                 fields=['date','low','close','money'],
                 include_now=True)
        log.info('len of arr: {}'.format(len(arr)))
        df = pd.DataFrame(arr)
        df.columns = ['date','low','close','money']
        log.info('get_bars: df: {}'.format(df.tail()))
        # current price
        # current_price = get_current_data()[g.security].last_price
        # log.info('price: {}'.format(current_price))
            
        # 取得过去60天的平均价格
        MA60 = df['close'].mean()
        log.info('ma60: {}'.format(MA60))
        # get avg money 10
        money_ma10 = df['money'].values[-10:].mean()
        log.info('avg amount 10: {}'.format(money_ma10))
        # get current money
        current_money = df['money'].values[-1]
        log.info('current_price: {}'.format(current_money))
        # 取得上一时间点价格
        current_price = df['close'].values[-1]
        log.info('current_money: {}'.format(current_price))
        # 取得当前的现金
        cash = context.portfolio.available_cash
    
        if security not in  g.bought_lists:
            # 如果上一时间点价格高出60天平均价, 则买入  1.618
            if current_price >= MA60 and current_money>= 1*money_ma10:
                # 记录这次买入
                log.warn('成交额为10日均量线的 {}倍'.format(current_money/money_ma10))
                log.warn("价格高于均价, 买入 %s" % (security))
                # 用 cash*0.1 or 100 买入股票
                order_value(security, 100, style=MarketOrderStyle)
                # bought_lists
                g.bought_lists.append(security)
        # 如果上一时间点价格低于60天平均价, 则空仓卖出
        elif current_price < MA60*0.9:
            # 记录这次卖出
            log.info("价格低于均价, 卖出 %s" % (security))
            # 卖出所有股票,使这只股票的最终持有量为0
            order_target(security, 0)
            # remove from bought_lists
            bought_lists.remove(security)


## 选股函数 break ma60
def check_stocks(context):
    # 获取沪深成分股
    g.available_list = get_available_stocks(context)
    
    # 获取股票的收盘价 ma60
    # close_data = attribute_history(security, 60, '1d', ['close'])
    # 取得过去60天的平均价格
    # MA60 = close_data['close'].mean()
    # 取得上一时间点价格
    # current_price = close_data['close'][-1]

    # Stocks = get_fundamentals(query(
    #         valuation.code,
    #         valuation.pb_ratio,
    #     ).filter(
    #         valuation.code.in_(security),
    #         valuation.pb_ratio < 2, #市净率低于2
            
    #     ))
    
    # 计算股票的负债比例
    # Stocks['Debt_Asset'] = Stocks['total_liability']/Stocks['total_assets']
    # 获取负债比率的市场均值
    # me = Stocks['Debt_Asset'].median()
    # 获取满足上述条件的股票列表
    # Codes = Stocks[Stocks['Debt_Asset'] > me].code

    return list(g.available_list)
    
###########################################   
## 过滤停股票/ST
def paused_filter(context, security_list):
    current_data = get_current_data()
    security_list = [stock for stock in security_list if not (current_data[stock].paused or current_data[stock].is_st)]
    # 返回结果
    return security_list

## 过滤退市股票
def delisted_filter(context, security_list):
    current_data = get_current_data()
    security_list = [stock for stock in security_list if not '退' in current_data[stock].name]
    # 返回结果
    return security_list

