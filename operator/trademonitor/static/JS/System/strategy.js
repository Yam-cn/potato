$(function () {
    oneSource = {
        data : []
    };
    twoSource = {
        data : []
    };
    threeSource = {
        data : []
    };

    taskRiskMonitors(0, 10);
    loadAccount();
    loadStrategy();
    loadTradeDetail();
    setTimeout("refreshAll()",refreshtime);
    /*$(window).resize(function () {
        var reload = false;
        tb_one.destroy(); tb_one = null;
        tb_two.destroy(); tb_two = null;
        tb_three.destroy(); tb_three = null;
        
        if (oneSource != null) {
            initTbOne(oneSource);
        }
        else
            reload = true;

        if (twoSource != null) {
            initTbTwo(twoSource);
        }
        else
            reload = true;

        if (threeSource != null) {
            initTbThree(threeSource);
        }
        else
            reload = true;
       
        if (reload)
            taskRiskMonitors(0, 10);
    });*/
});

function taskRiskMonitors(start, length) {
    if (tb_one == null) {
        initTbOne(oneSource);
    }
    else
        tb_one.clear().rows.add(oneSource.data).draw();

    if (tb_two == null) {
        initTbTwo(twoSource);
    }
    else
        tb_two.clear().rows.add(twoSource.data).draw();

    if (tb_three == null) {
        initTbThree(threeSource);
    }
    else
        tb_three.clear().rows.add(threeSource.data).draw();
    initclick();
}
//添加账户
function addTableOne(){
    var rowobj = $.extend({},account_info)
    rowobj.account_id = '<input value="AccountId" class="form-control textbx" style="float : left;"/>';
    rowobj.account_type = '<select class="form-control textbx">' +
                        '<option value="CTP"> CTP</option>' +
                        '</select>';
    rowobj.dyn_right = "--";
    rowobj.cash_avalible = "--";
    rowobj.cash_frozen = "--";
    rowobj.asset = "--";
    rowobj.date = "--";
    var arr = [];
    arr.push(rowobj);
    tb_one.rows.add(arr).draw();
}
//保存账户
function saveTableOne(){
    var rowobj = tb_one.row(tb_one.$('tr.selected')).data();
    if(typeof rowobj == 'undefined'){
        showAlert("请选择账户");
        return;
    }
    if(typeof tb_one.$('tr.selected').children()[0].getElementsByTagName("input")[0] === 'undefined'){
        return;
    }
    var acc = tb_one.$('tr.selected').children()[0].getElementsByTagName("input")[0].value;
    var acctype = tb_one.$('tr.selected').children()[1].getElementsByTagName("select")[0].value;
    rowobj.account_id = acc;
    rowobj.account_type = acctype;
    $.ajax({
        url: "/addAccount",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    if(rdata[0] == '1'){
		        showAlert("账户已存在");
		    }else{
		        AccountList.push(rdata[0]);
		        AccountTimerList.push(getAccountTimer(rdata[0]));
		        showAlert("账户添加成功");
		    }
            return;
		}
    });
}
//删除账户
function deletTableOne(){
    var rowobj = tb_one.row(tb_one.$('tr.selected')).data();
    if(typeof rowobj == 'undefined'){
        showAlert("请选择账户");
        return;
    }
    $.ajax({
        url: "/deleteAccount",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return;
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    if(rdata[0] == '0'){
		        showAlert("账户ID为空，删除失败");
                return;
		    }
            tb_one.row('.selected').remove().draw( false );
            removeListItem(rdata[0],AccType);
            showAlert("账户已删除");
            return;
		}
    });
}
//添加策略
function addTableTwo(){
    var rowobj = $.extend({},strategy_info)
    rowobj.strategy_id = "";
    rowobj.strategy_name = '<input value="策略名称" class="form-control textbx"/>';
    rowobj.ticker = '<input value="交易品种" class="form-control textbx"/>';
    rowobj.position_lot = "--";
    rowobj.strategy_profit = "--";
    rowobj.position_profit = "--";
    rowobj.args = '<input value="arg0,arg1..." class="form-control textbx"/>';
    rowobj.account_id = getAccountIDSelect("");
    rowobj.filename = '<input value="filename" class="form-control textbx"/>';
    rowobj.status = "--";
    rowobj.date = "";
    var arr = [];
    $.ajax({
        url: "/genuuid",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: {},
		timeout: 5000,
		fail: function(e) {
			return
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
            rowobj.strategy_id = rdata[0];
		    arr.push(rowobj);
		    tb_two.rows.add(arr).draw();
            return;
		}
    });
}
//保存策略/生效
function saveTableTwo(){
    var rowobj = tb_two.row(tb_two.$('tr.selected')).data();
    if(typeof rowobj == 'undefined'){
        showAlert("请选择策略");
        return;
    }
    if(typeof tb_two.$('tr.selected').children()[1].getElementsByTagName("input")[0] === 'undefined'){
        return;
    }
    var strategyid = tb_two.$('tr.selected').children()[0].getElementsByTagName("input")[0].value;
    var strategyname = tb_two.$('tr.selected').children()[1].getElementsByTagName("input")[0].value;
    var tradetype = tb_two.$('tr.selected').children()[2].getElementsByTagName("input")[0].value;
    var args = tb_two.$('tr.selected').children()[6].getElementsByTagName("input")[0].value;
    var accid = tb_two.$('tr.selected').children()[7].getElementsByTagName("select")[0].value;
    var filename = tb_two.$('tr.selected').children()[8].getElementsByTagName("input")[0].value;
    rowobj.strategy_id = strategyid;
    rowobj.strategy_name = strategyname;
    rowobj.ticker = tradetype;
    rowobj.args = args;
    rowobj.account_id = accid;
    rowobj.filename = filename;
    var strategy_id = rowobj.strategy_id;
    $.ajax({
        url: "/addStrategy",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return;
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    addTableThree(strategy_id,strategyname);
            showAlert("策略添加成功");
            return;
		}
    });
}
//停止策略
function stopTableTwo(){
    var rowobj = tb_two.row(tb_two.$('tr.selected')).data();
    if(typeof rowobj == 'undefined'){
        showAlert("请选择策略");
        return;
    }
    $.ajax({
        url: "/stopStrategy",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    showAlert("策略已停止");
            return;
		}
    });
}
//删除策略
function deletTableTwo(){
    var rowobj = tb_two.row(tb_two.$('tr.selected')).data();
    if(typeof rowobj == 'undefined'){
        showAlert("请选择策略");
        return;
    }
    $.ajax({
        url: "/deleteStrategy",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return;
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    if(rdata[0] == '0'){
		        showAlert("策略ID为空，删除失败");
                return;
		    }
            tb_two.row('.selected').remove().draw( false );
            removeListItem(rdata[0],StrType);
            showAlert("策略已删除");
            return;
		}
    });
}
//添加详情
function addTableThree(strategy_id,strategy_name){
    var rowobj = $.extend({},trade_detail)
    rowobj.strategy_id = strategy_id;
    rowobj.strategy_name = strategy_name;
    rowobj.ticker = "--";
    rowobj.trade_price = "--";
    rowobj.trade_amount = "--";
    rowobj.trade_datetime = "--";
    var arr = [];
    arr.push(rowobj);

    $.ajax({
        url: "/addTradeDetail",
        dataType: "JSON",
        cache: false,
        type: 'GET',
		data: rowobj,
		timeout: 5000,
		fail: function(e) {
			return
		},
		error: function(e) {
			return;
		},
		success:function(rdata) {
		    tb_three.rows.add(arr).draw();
            return;
		}
    });
}
//删除详情
function deleteTableThree(){
    tb_three.row('.selected').remove().draw( false );
}
function initclick(){
     $('#tb_one tbody').on('click','tr', function(){
         if ( $(this).hasClass('selected') ) {
             $(this).removeClass('selected');
             $(this).find('td').css('background-color', '#000');
     }
     else {
       tb_one.$('tr.selected').removeClass('selected');
       $(this).addClass('selected');
              $(tb_one.cells().nodes()).css('background-color', '#000');
              $(this).find('td').css('background-color', '#410080');
     }
     });
     $('#tb_two tbody').on('click','tr', function(){
         if ( $(this).hasClass('selected') ) {
             $(this).removeClass('selected');
             $(this).find('td').css('background-color', '#000');
     }
     else {
       tb_two.$('tr.selected').removeClass('selected');
       $(this).addClass('selected');
              $(tb_two.cells().nodes()).css('background-color', '#000');
              $(this).find('td').css('background-color', '#410080');
     }
     });
     $('#tb_three tbody').on('click','tr', function(){
         if ( $(this).hasClass('selected') ) {
             $(this).removeClass('selected');
             $(this).find('td').css('background-color', '#000');
     }
     else {
       tb_three.$('tr.selected').removeClass('selected');
       $(this).addClass('selected');
              $(tb_three.cells().nodes()).css('background-color', '#000');
              $(this).find('td').css('background-color', '#410080');
     }
     });
}

function initColor() {
    var lastIdx = null;
    $('#tb_one tbody')
    .on('mouseenter', 'td', function () {
        var colIdx = tb_one.cell(this).index().column;
        var rowIdx = tb_one.cell(this).index().row;
        if (colIdx !== lastIdx) {
            $(tb_one.cells().nodes()).css('background-color', '#000');
            $(tb_one.row(rowIdx).nodes()).find("td").css('background-color', '#410080');
        }
    })
    .on('mouseleave', function () {
        $(tb_one.cells().nodes()).css('background-color', '#000');
    });

    $('#tb_two tbody')
    .on('mouseenter', 'td', function () {
        var colIdx = tb_two.cell(this).index().column;
        var rowIdx = tb_two.cell(this).index().row;
        if (colIdx !== lastIdx) {
            $(tb_two.cells().nodes()).css('background-color', '#000');
            $(tb_two.row(rowIdx).nodes()).find("td").css('background-color', '#410080');
        }
    })
    .on('mouseleave', function () {
        $(tb_one.cells().nodes()).css('background-color', '#000');
    });

    $('#tb_three tbody')
    .on('mouseenter', 'td', function () {
        var colIdx = tb_three.cell(this).index().column;
        var rowIdx = tb_three.cell(this).index().row;
        if (colIdx !== lastIdx) {
            $(tb_three.cells().nodes()).css('background-color', '#000');
            $(tb_three.row(rowIdx).nodes()).find("td").css('background-color', '#410080');
        }
    })
    .on('mouseleave', function () {
        $(tb_one.cells().nodes()).css('background-color', '#000');
    });
}

function initTbOne(dataSet) {
    tb_one = $('#tb_one')
            .DataTable(
                    {
                        "lengthChange": false,
                        "processing": false,
                        "paging": false,
                        "scrollY": "200px",
                        "searching": false,
                        "serverSide": false,
                        "stateSave": false,
                        "ordering": true,
                        "info": false,
                        "ajax": function (data, callback, settings) {
                            callback(dataSet);
                        },
                        "columns": [
                                {
                                    "data": "account_id",
                                    "width": "9%",
                                    "render": function (data, type, full, meta) {
                                        return  '<label style="float : left;">' + data + '</label>';
                                    }
                                },
                                {
                                    "data": "account_type",
                                    "width": "9%"
                                },
                                {
                                    "data": "dyn_right",
                                    "width": "9%"
                                },
                                {
                                    "data": "cash_avalible",
                                    "width": "9%"
                                },
                                {
                                    "data": "cash_frozen",
                                    "width": "9%"
                                },
                                {
                                    "data": "asset",
                                    "width": "9%"
                                },
                                {
                                    "data": "date",
                                    "width": "9%"
                                }]
                    });
}

function initTbTwo(dataSet) {
    tb_two = $('#tb_two')
            .DataTable(
                    {
                        "bAutoWidth":true,
                        "lengthChange": false,
                        "processing": false,
                        "paging": false,
                        "searching": false,
                        "serverSide": false,
                        "scrollY": "200px",
                        "stateSave": false,
                        "ordering": true,
                        "info": false,
                        "ajax": function (data, callback, settings) {
                            callback(dataSet);
                        },
                        "buttons": [
                            {
                                extend: 'ttntn',
                                text: 'Office info',
                                show: '.office',
                                hide: '.tt'
                            },
                            {
                                extend: 'ttntn',
                                text: 'HR info',
                                show: '.tt',
                                hide: '.office'
                            }
                        ],
                        "columns": [
                                {
                                    "data": "strategy_id",
                                    "width": "9%",
                                    "render": function (data, type, full, meta) {
                                        var shtml = "";
                                        if(ShowFlag_Tbtwo){
                                            shtml += '<label style="color : #DDD666; float : left;">' + data + '</label>';
                                            shtml += '<input type="hidden" value='+ data +'/>';
                                        }else{
                                            shtml += '<label style="color : #DDD666; float : left;">+</label>';
                                            shtml += '<input type="hidden" value='+ data +'/>';
                                        }
                                        return shtml;
                                    }
                                },
                                {
                                    "data": "strategy_name",
                                    "width": "9%"
                                },
                                {
                                    "data": "ticker",
                                    "width": "9%"
                                },
                                {
                                    "data": "position_lot",
                                    "width": "9%"
                                },
                                {
                                    "data": "strategy_profit",
                                    "width": "9%"
                                },
                                {
                                    "data": "position_profit",
                                    "width": "9%"
                                },
                                {
                                    "data": "args",
                                    "width": "9%"
                                },
                                {
                                    "data": "account_id",
                                    "width": "9%"
                                },
                                {
                                    "data": "filename",
                                    "width": "9%"
                                },
                                {
                                    "data": "status",
                                    "width": "9%"
                                },
                                {
                                    "data": "date",
                                    "width": "9%"
                                }]
                    });
}

function initTbThree(dataSet) {
    tb_three = $('#tb_three')
            .DataTable(
                    {
                        "lengthChange": false,
                        "processing": false,
                        "paging": false,
                        "searching": false,
                        "serverSide": false,
                        "stateSave": false,
                        "scrollY": "200px",
                        "ordering": true,
                        "info": false,
                        "ajax": function (data, callback, settings) {
                            callback(dataSet);
                        },
                        "columns": [
                                {
                                    "data": "strategy_id",
                                    "width": "9%",
                                    "render": function (data, type, full, meta) {
                                        var shtml = "";
                                        if(ShowFlag_Tbthree){
                                            shtml += '<label style="color : #DDD666; float : left;">' + data + '</label>';
                                            shtml += '<input type="hidden" value="'+ data +'" />'
                                        }else{
                                            shtml += '<label style="color : #DDD666; float : left;">+</label>';
                                            shtml += '<input type="hidden" value="'+ data +'" />'
                                        }
                                        return shtml;
                                    }
                                },
                                {
                                    "data": "strategy_name",
                                    "width": "9%"
                                },
                                {
                                    "data": "ticker",
                                    "width": "9%"
                                },
                                {
                                    "data": "trade_price",
                                    "width": "9%"
                                },
                                {
                                    "data": "trade_amount",
                                    "width": "9%"
                                },
                                {
                                    "data": "trade_datetime",
                                    "width": "9%"
                                }]
                    });
}
function ShowTableTwo(){
    if(ShowFlag_Tbtwo){
        ShowFlag_Tbtwo = false;
        var tdata = tb_two.data();
        for(var i = 0; i < tdata.length; i++ ){
            var nodelist = $(tb_two.row(i).node()).children();
            var shtml = '<label style="color : #DDD666; float : left;">+</label>';
            shtml += '<input type="hidden" value="'+ tdata[i].strategy_id +'" />'
            nodelist[0].innerHTML = shtml;
        }
        $("#TbTwoShow").text("展开ID");
        tb_two.columns.adjust().draw();
    }
    else{
        ShowFlag_Tbtwo = true;
        var tdata = tb_two.data();
        for(var i = 0; i < tdata.length; i++ ){
            var nodelist = $(tb_two.row(i).node()).children();
            var shtml = '<label style="color : #DDD666; float : left;">' + tdata[i].strategy_id + '</label>';
            shtml += '<input type="hidden" value="'+ tdata[i].strategy_id +'" />'
            nodelist[0].innerHTML = shtml;
        }
        $("#TbTwoShow").text("隐藏ID");
        tb_two.columns.adjust().draw();
    }
}
function ShowTableThree(){
    if(ShowFlag_Tbthree){
        ShowFlag_Tbthree = false;
        var tdata = tb_three.data();
        for(var i = 0; i < tdata.length; i++ ){
            var nodelist = $(tb_three.row(i).node()).children();
            var shtml = '<label style="color : #DDD666; float : left;">+</label>';
            shtml += '<input type="hidden" value="'+ tdata[i].strategy_id +'" />'
            nodelist[0].innerHTML = shtml;
        }
        $("#TbThreeShow").text("展开ID");
        tb_three.columns.adjust().draw();
    }
    else{
        ShowFlag_Tbthree = true;
        var tdata = tb_three.data();
        for(var i = 0; i < tdata.length; i++ ){
            var nodelist = $(tb_three.row(i).node()).children();
            var shtml = '<label style="color : #DDD666; float : left;">' + tdata[i].strategy_id + '</label>';
            shtml += '<input type="hidden" value="'+ tdata[i].strategy_id +'" />'
            nodelist[0].innerHTML = shtml;
        }
        $("#TbThreeShow").text("隐藏ID");
        tb_three.columns.adjust().draw();
    }
}

