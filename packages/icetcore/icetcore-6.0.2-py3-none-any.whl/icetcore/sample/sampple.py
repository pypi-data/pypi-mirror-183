import time
from icetcore import TCoreAPI,QuoteEvent,TradeEvent,OrderStruct,BarType,GreeksType

class APIEvent(TradeEvent,QuoteEvent):
    #连线成功通知apitype="quoteapi"是行情api的通知，"tradeapi"是交易通知
    def onconnected(self,apitype:str):
        print(apitype)
    #断线成功通知
    def ondisconnected(self,apitype:str):
        print(apitype)
    #subATM订阅的ATM合约信息，动态推送期权的ATM平值,OTM-1C虚值一档认购，OTM-1P虚值一档认沽，和认购期权合约列表
    def onATM(self,datatype,symbol,data:dict):
        pass
    #
    def ongreeksreal(self,datatype,symbol,data:dict):
        pass
    #subquote订阅的合约实时行情
    def onquote(self,data):
        #print(data)
        pass
    #subbar订阅的动态K线数据
    def onbar(self,datatype,interval,symbol,data:list,isreal:bool):
        # print("onbar",self._tcoreapi.getsymbol_session("TC.F.SHFE.rb.HOT"))
        # print("############\n",datatype,"  ",interval,"  ",data[1],"\n",data[2],"\n",data[3])
        print("$$$$$$$$$$$$$$$$$$$$$$\n",datatype,"  ",interval,"  ",data[-3],"\n",data[-2],"\n",data[-1])
        print(data[-1])
    #server与本机时间差
    def onservertime(self, serverdt):
        print("!!!!!!!!!!!!!!!",serverdt)
        pass
    # #实时委托信息
    # def onordereportreal(self,data):
    #     print(data)
    # #实时成交信息
    # def onfilledreportreal(self,data):
    #     print(data)
    #账户登出登入时委托资料需要清理通知
    def onorderreportreset(self):
        print("onorderreportreset")
    # #期权持仓监控信息
    # def onpositionmoniter(self,data):
    #     print(data)


#事件消息需要继承api中QuoteEvent和TradeEvent类，并重写对应方法，即可在对应的回调方法收到实时更新事件
#TCoreAPI参数也可以不带入事件类名，不带入事件类就无法收到实时消息，只能使用同步接口方法
api=TCoreAPI(APIEvent)#
re=api.connect()
time.sleep(1)
#获取所有合约，可指定类型FUT/OPT/STK，指定交易所
print(api.getallsymbol())
#获取合约最小跳动
print(api.getsymbol_ticksize("TC.F.SHFE.rb.HOT"))
#获取合约交易时段
print(api.getsymbol_session("TC.F.SHFE.rb.HOT"))
# #订阅动态K线数据
# api.subbar(BarType.MINUTE,"TC.F.SHFE.rb.HOT",start="2022120101")
# api.subbar(BarType.MINUTE,"TC.F.SHFE.cu.HOT",start="2022120101")
#获取已登入账户列表
accoutlist=api.getaccoutlist()
print(accoutlist)
#获取合约持仓
print(api.getposition("CTP_NHGPQQ_SIM-8050-90096859"))
#获取当天全部委托
print(api.getorderreport())
#获取热门月列表，填入时间时返回对应时间的热门对应指定月合约，Key是换月时间，value是指定月
print(api.gethotmonth("TC.F.SHFE.rb.HOT"))

##下单
OrderStruct.Account=accoutlist[0]["Account"]
OrderStruct.BrokerID=accoutlist[0]["BrokerID"]
OrderStruct.Symbol="TC.F.DCE.i.202301"
OrderStruct.Side=1
OrderStruct.OrderType=2
OrderStruct.PositionEffect=0
OrderStruct.TimeInForce=1
OrderStruct.Price=848
OrderStruct.OrderQty=1
ordkey=api.neworder(OrderStruct)
print(ordkey)
if ordkey!=None:
    while True:
        if api.getorderinfo(ordkey):
            print("#####################新增委托：",api.getorderinfo(ordkey)['ReportID'])#,TCoreAPI.QryReport()[-1]['ReportID'])
            break

##改单
api.replaceorder('4112047019F',price=839)
# 获取历史合约信息
print(api.getsymbolhistory("OPT","20221213"))

# print(api.gethotmonth("TC.F.CFFEX.T.HOT"))
# print(api.gethotmonth("TC.F.CFFEX.T.HOT","20221223","0900"))


#获取合约交易时段
#print(api.getsymbol_session("TC.F.SHFE.rb.HOT"))
# #订阅动态K线数据
# print(datetime.now())
print(api.getquotehistory(BarType.MINUTE,5,"TC.F.SHFE.au.HOT",starttime="2022120101"))
# print(datetime.now())
#print(api.getgreekshistory(GreeksType.DOGSK,"TC.O.SSE.510050.202212.C.2.5","2022120200","2022120207"))
#api.subgreeksreal("TC.O.SSE.510050.202212.C.2.5")
api.subquote("TC.O.SSE.510050.202212.C.2.5")
# api.subbar(BarType.MINUTE,5,"TC.F.CFFEX.T.HOT",starttime="2022120101")
# api.subbar(BarType.MINUTE,5,"TC.F.SHFE.rb.HOT",starttime="2022120101")
# api.subbar(BarType.MINUTE,5,"TC.F.SHFE.cu.HOT",starttime="2022120101")
#获取ATM
        # -2:实值两档期权合约
        # -1:实值一档期权合约
        #  0:平值期权合约
        #  1:虚值期权合约
print(api.getATM("TC.O.SSE.510050.202212.C",2))

api.join()
