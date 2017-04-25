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
            AccountTimerList.length = 0;
            if(typeof rdata != 'undefined' && rdata.length > 0){
                for(var i = 0; i < rdata.length; i++){
                    var oitem = rdata[i];
                    AccountList.push(oitem.account_id);
                    AccountTimerList.push(getAccountTimer(oitem.account_id));
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
            StrategyTimerList.length = 0;
            if(typeof rdata != 'undefined' && rdata.length > 0){
                for(var i = 0; i < rdata.length; i++){
                    var oitem = rdata[i];
                    StrategyList.push(oitem.strategy_id);
                    StrategyTimerList.push(getStrategyTimer(oitem.strategy_id));
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
//获取账户定时任务 传入账户ID参数
function getAccountTimer(uuid){
    return {
        id: uuid,
        enable: 1,
        refreshhandler: function(){
            var param = {
                account_id : this.id
            }
            if(this.enable == 1){
                $.ajax({
                    url: "/queryAccount",
                    dataType: "JSON",
                    cache: false,
                    type: 'GET',
                    data: param,
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
                        if(typeof rdata === "undefined" || rdata === null || rdata.length <= 0){
                            return;
                        }
                        //取全部已显示的数据，遍历，找出和本次刷新的account_id相同的记录
                        //然后把对应的新数据更新到这一行
                        var tdata = tb_one.data();
                        for(var i = 0; i < tdata.length; i++ ){
                            if(param.account_id === tdata[i].account_id){
                                var nodelist = $(tb_one.row(i).node()).children();
                                nodelist[0].innerHTML = rdata[0].account_id;
                                nodelist[1].innerHTML = rdata[0].account_type;
                                nodelist[2].innerHTML = rdata[0].dyn_right;
                                nodelist[3].innerHTML = rdata[0].cash_avalible;
                                nodelist[4].innerHTML = rdata[0].cash_frozen;
                                nodelist[5].innerHTML = rdata[0].asset;
                                nodelist[6].innerHTML = rdata[0].date;
                                break;
                            }
                        }
                        return;
                    }
                });
            }
        }
    };
}
//获取策略定时任务 传入策略ID参数
function getStrategyTimer(uuid){
    return {
        id: uuid,
        enable: 1,
        refreshhandler: function(){
            var self = this;
            var param = {
                strategy_id : this.id
            }
            if(this.enable == 1){
                $.ajax({
                    url: "/queryStrategy",
                    dataType: "JSON",
                    cache: false,
                    type: 'GET',
                    data: param,
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
                        if(typeof rdata === "undefined" || rdata === null || rdata.length <= 0){
                            return;
                        }
                        /*if(rdata.status === "Y"){
                            self.enable = 1;
                        }else{
                            self.enable = 0;
                        }*/
                        //取全部已显示的数据，遍历，找出和本次刷新的account_id相同的记录
                        //然后把对应的新数据更新到这一行
                        var tdata = tb_two.data();
                        for(var i = 0; i < tdata.length; i++ ){
                            if(param.strategy_id === tdata[i].strategy_id){
                                var nodelist = $(tb_two.row(i).node()).children();
                                var shtml = '';
                                if(ShowFlag_Tbtwo){
                                    shtml += '<label style="color : #DDD666; float : left;">' + rdata[0].strategy_id + '</label>';
                                    shtml += '<input type="hidden" value="'+ rdata[0].strategy_id +'" />'
                                }else{
                                    shtml += '<label style="color : #DDD666; float : left;">+</label>';
                                    shtml += '<input type="hidden" value="'+ rdata[0].strategy_id +'" />'
                                }
                                nodelist[0].innerHTML = shtml;
                                nodelist[1].innerHTML = rdata[0].strategy_name;
                                nodelist[2].innerHTML = rdata[0].ticker;
                                nodelist[3].innerHTML = rdata[0].position_lot;
                                nodelist[4].innerHTML = rdata[0].strategy_profit;
                                nodelist[5].innerHTML = rdata[0].position_profit;
                                nodelist[6].innerHTML = rdata[0].args;
                                nodelist[7].innerHTML = rdata[0].account_id;
                                nodelist[8].innerHTML = rdata[0].filename;
                                nodelist[9].innerHTML = rdata[0].status;
                                nodelist[10].innerHTML = rdata[0].date;
                                break;
                            }
                        }
                        return;
                    }
                });
            }
        }
    };
}
//获取详细定时任务 传入策略ID参数
function getTradeDetailTimer(uuid){
    return {
        id: uuid,
        enable: 1,
        refreshhandler: function(){
            var param = {
                strategy_id : this.id
            }
            if(this.enable == 1){
                $.ajax({
                    url: "/queryTradeDetail",
                    dataType: "JSON",
                    cache: false,
                    type: 'GET',
                    data: param,
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
                        if(typeof rdata === "undefined" || rdata === null || rdata.length <= 0){
                            return;
                        }
                        //取全部已显示的数据，遍历，找出和本次刷新的account_id相同的记录
                        //然后把对应的新数据更新到这一行
                        var tdata = tb_three.data();
                        return;
                    }
                });
            }
        }
    };
}
//定时刷新
function refreshAll(){
    for(var i=0;i<AccountTimerList.length;i++){
        var item = AccountTimerList[i];
        if(item.enable == 1){
            item.refreshhandler();
        }
    }
    for(var i=0;i<StrategyTimerList.length;i++){
        var item = StrategyTimerList[i];
        if(item.enable == 1){
            item.refreshhandler();
        }
    }
    //策略详细信息采用全部统一刷新
    loadTradeDetail();
    /*for(var i=0;i<TradeDetailTimerList.length;i++){
        var item = TradeDetailTimerList[i];
        if(item.enable == 1){
            item.refreshhandler();
        }
    }*/
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