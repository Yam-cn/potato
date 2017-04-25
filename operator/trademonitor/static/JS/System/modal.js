function showAlert(stext,stitle){
	 $('#myModal').on('show.bs.modal', function (event) {
        var modal = $(this)
        if(typeof stitle !== "undefined")
            modal.find('.modal-title').text(stitle)
        modal.find('.modal-body').text(stext)
    }).modal('show')
}