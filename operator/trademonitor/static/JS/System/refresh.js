//加载已有账户
function loadAccount(){
    $.ajax({
        url: "/queryAllAccount",
        dataType: "JSON",
        cache: false,
        type: 'GET',
        data: {},
        timeout: 5000,
        fail: function(e) {
            return;
        },
        error: function(e) {
            return;
        },
        success:function(rdata) {
            if(typeof rdata === 'string')
                rdata = JSON.parse(rdata);
            AccountList.length = 0;
            if(typeof rdata != 'undefined' && rdata.length > 0){
                for(var i = 0; i < rdata.length; i++){
                    var oitem = rdata[i];
                    AccountList.push(oitem.account_id);
                }
            }
            tb_one.clear().rows.add(rdata).draw();
            return;
        }
    });
}
//加载已有策略
function loadStrategy(){
    $.ajax({
        url: "/queryAllStrategy",
        dataType: "JSON",
        cache: false,
        type: 'GET',
        data: {},
        timeout: 5000,
        fail: function(e) {
            return;
        },
        error: function(e) {
            return;
        },
        success:function(rdata) {
            if(typeof rdata === 'string')
                rdata = JSON.parse(rdata);
            StrategyList.length = 0;
            if(typeof rdata != 'undefined' && rdata.length > 0){
                for(var i = 0; i < rdata.length; i++){
                    var oitem = rdata[i];
                    StrategyList.push(oitem.strategy_id);
                }
            }
            tb_two.clear().rows.add(rdata).draw();
            return;
        }
    });
}
//加载已有策略详细信息 最近20条
function loadTradeDetail(){
    $.ajax({
        url: "/queryAllTradeDetail",
        dataType: "JSON",
        cache: false,
        type: 'GET',
        data: {},
        timeout: 5000,
        fail: function(e) {
            return;
        },
        error: function(e) {
            return;
        },
        success:function(rdata) {
            if(typeof rdata === 'string')
                rdata = JSON.parse(rdata);
            tb_three.clear().rows.add(rdata).draw();
            return;
        }
    });
}
//定时刷新
function refreshAll(){
    //账户信息采用全部统一刷新
    loadAccount();
    //策略信息采用全部统一刷新
    loadStrategy();
    //策略详细信息采用全部统一刷新
    loadTradeDetail();
    refTimer = setTimeout("refreshAll()",refreshtime);
}
//根据id删除指定条目
//id:账户id或者策略id  idtype：账户/策略/详细
function removeListItem(id,idtype){
    if(idtype === AccType){
        var slen = AccountList.length;
        for(var i = 0; i < slen; i++){
            if(id === AccountList[i]){
                AccountList.splice(i,1);
                break;
            }
        }
        var slen1 = AccountTimerList.length;
        for(var i = 0; i < slen1; i++){
            if(id === AccountTimerList[i].id){
                AccountTimerList.splice(i,1);
                break;
            }
        }
    }else if(idtype === StrType){
        var slen = StrategyList.length;
        for(var i = 0; i < slen; i++){
            if(id === StrategyList[i]){
                StrategyList.splice(i,1);
                break;
            }
        }
        var slen1 = StrategyTimerList.length;
        for(var i = 0; i < slen1; i++){
            if(id === StrategyTimerList[i].id){
                StrategyTimerList.splice(i,1);
                break;
            }
        }
    }else if(idtype === TraType){
        var slen = TransDetailList.length;
        for(var i = 0; i < slen; i++){
            if(id === TransDetailList[i]){
                TransDetailList.splice(i,1);
                break;
            }
        }
        var slen1 = TradeDetailTimerList.length;
        for(var i = 0; i < slen1; i++){
            if(id === TradeDetailTimerList[i].id){
                TradeDetailTimerList.splice(i,1);
                break;
            }
        }
    }else{
    }
}
function getAccountIDSelect(accid){
    var shtml = '<select class="form-control textbx">';
    for(var i = 0; i < AccountList.length; i++){
        if(accid === AccountList[i]){
            shtml += '<option selected = "selected" value="' + AccountList[i] + '">';
            shtml += AccountList[i];
            shtml += '</option>';
        }
        shtml += '<option value="' + AccountList[i] + '">';
        shtml += AccountList[i];
        shtml += '</option>';
    }
    shtml += '</select>';
    return shtml;
}
//策略运行状态转化为中文
function getStrategyStatus(strid){
    if(typeof strid === 'undefined' || strid === ''){
        return '';
    }
    if(strid == StrPending){
        return CHStrPending;
    }else if(strid == StrStarted){
        return CHStrStarted;
    }else if(strid == StrRetry){
        return CHStrRetry;
    }else if(strid == StrFailure){
        return CHStrFailure;
    }else if(strid == StrSuccess){
        return CHStrSuccess;
    }else{
        return '';
    }
}
