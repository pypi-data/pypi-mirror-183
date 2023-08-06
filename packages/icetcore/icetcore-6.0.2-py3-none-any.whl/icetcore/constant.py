"""
General constant enums used in the trading platform.
"""

from enum import Enum
from dataclasses import dataclass

@dataclass
class OrderStruct:
    Account:str
    BrokerID:str
    Symbol:str
    Side:int
    OrderQty:int
    OrderType:int
    TimeInForce:int
    PositionEffect:int
    SymbolA:str=""
    SymbolB:str=""
    Price:int=0
    StopPrice:str=""
    Side1:int=0
    Side2:int=0
    ContingentSymbol:str=""
    TrailingAmount:int=0
    TrailingField:int=0
    TrailingType:int=0
    TouchCondition:int=0
    TouchField:int=0
    TouchPrice:str=""
    Synthetic:int=0
    GroupID:str=""
    GroupType:int=0
    GrpAcctOrdType:int=0
    ChasePrice:str=""
    Strategy:str=""
    UserKey1:str=""
    UserKey2:str=""
    UserKey3:str=""
    SlicedPriceField:int=0
    SlicedTicks:int=0
    SlicedType:int=0
    DiscloseQty:int=0
    Variance:int=0
    Interval:int=0
    LeftoverAction:int=0
    SelfTradePrevention:int=0
    ExtCommands:str=""
    ExCode:str=""
    Exchange:str=""
    TradeType:int=0

class SymbolType():
    Options="OPT"
    Futures="FUT"
    Stocks="STK"

class BarType():
    MINUTE = 4
    DK = 5
    TICK = 2
class GreeksType():
    DOGSS=800
    DOGSK=820
    GREEKS1K=9
    GREEKSTICK=10
    GREEKSDK=19
