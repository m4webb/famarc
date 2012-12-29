//on load
$(function() {

    $('#file_table').dataTable( {
        "bProcessing" : true,
        "sAjaxSource" : "/file_table.json",
        "sDom" : 'ftr',
        "sScrollY": "400px", 
        "bPaginate": false,
        "aoColumnDefs": [
              { "sClass": "id", 
                "aTargets": [ "id" ] 
              }
            ],
        "fnCreatedRow": function( nRow, aData, iDataIndex ) {
            $(nRow).click( function() {
                window.open('/files/' + $(nRow).find('.id').html());
            });
        }, 
    } );

});
