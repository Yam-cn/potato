function showAlert(stext,stitle){
	 $('#AlertModal').on('show.bs.modal', function (event) {
        var modal = $(this)
        if(typeof stitle !== "undefined")
            modal.find('.modal-title').text(stitle)
        modal.find('.modal-body').text(stext)
    }).modal('show')
}
function showConfirm(stext,stitle){
	 $('#ConfirmModal').on('show.bs.modal', function (event) {
        var modal = $(this)
        if(typeof stitle !== "undefined")
            modal.find('.modal-title').text(stitle)
        modal.find('.modal-body').text(stext)
    }).modal('show')
}
function EditAccountId(stext){
	 $('#EditAccountId').on('show.bs.modal', function (event) {
        var modal = $(this)
        if(typeof stitle !== "undefined")
            modal.find('.modal-title').text(stitle)
    }).modal('show')
}
function EditStrategy(stext){
    var shtml = getAccountIDSelectV2();
    if(typeof shtml === "undefined" || shtml === ""){
        shtml = '<input type="text" id="accid" class="form-control"/>';
    }
    $("#divaccid").html("").append(shtml);
	 $('#EditStrategy').on('show.bs.modal', function (event) {
        var modal = $(this)
        if(typeof stitle !== "undefined")
            modal.find('.modal-title').text(stitle)
    }).modal('show')
}
function SubmitAccountId(){
    $('#EditAccountId').modal('hide');
    saveTableOne();
}
function SubmitStrategy(){
    $('#EditStrategy').modal('hide');
    saveTableTwo();
}
function SubmitStopAllStr(){
    $('#ConfirmModal').modal('hide');
    stopAllStrategy();
}
function getAccountIDSelectV2(){
    var shtml = '<select class="form-control" id="accid">';
    if(AccountList.length <= 0){
        return "";
    }
    for(var i = 0; i < AccountList.length; i++){
        shtml += '<option value="' + AccountList[i] + '">';
        shtml += AccountList[i];
        shtml += '</option>';
    }
    shtml += '</select>';
    return shtml;
}