//on load
$(function() {

    var file_tags_table = $('#file_tags').dataTable( {
        "bProcessing" : true,
        "sAjaxSource" : window.location.pathname + "/file_tags.json",
        "sDom" : 'tr',
        "sScrollY": "100px", 
        "bPaginate": true,
        "aoColumnDefs": [
              { "sClass": "id", 
                "aTargets": [ "id" ] 
              }
            ],
    } );

    $('#tag_form').submit(function() {
        $.post(window.location.pathname + "/addtag", $('#tag_form').serialize(), function(data) {
            file_tags_table.fnReloadAjax( window.location.pathname + "/file_tags.json");
            $('#newtag').val("");
        });
        return false;
    });

    $('#tag_form input').keydown(function(e) {
        if (e.keyCode == 13) {
            e.preventDefault();
            $('#tag_form').submit();
       }
    });

});
