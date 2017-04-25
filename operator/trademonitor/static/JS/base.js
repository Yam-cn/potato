var serverURL = "";
var quanta_ip = '192.168.212.28';
var quanta_socket = "8080";
var refreshtime = 5000;//刷新时间
var AccountList = [];//账户列表
var StrategyList = [];//策略列表
var TransDetailList = [];//详细信息列表
var AccountTimerList = [];//账户定时任务列表
var StrategyTimerList = [];//策略定时任务列表
var TradeDetailTimerList = [];//详细定时任务列表
var refTimer;//定时任务刷新定时器
var tb_one,tb_two,tb_three, allSource, oneSource, twoSource, threeSource;

var AccType = "A"; //ID类型：账户
var StrType = "S"; //ID类型：策略
var TraType = "A"; //ID类型：交易详细

var ShowFlag_Tbtwo = true; //是否显示策略ID
var ShowFlag_Tbthree = true; //是否显示策略ID