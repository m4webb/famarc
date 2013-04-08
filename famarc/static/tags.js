//on load
$(function() {

    $('#tags_table').dataTable( {
        "bProcessing" : true,
        "sAjaxSource" : "/tags_table.json",
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
                window.open('/tags/' + $(nRow).find('.id').html(), "_self");
            });
            //$('td', nRow).attr('nowrap', 'nowrap');
            return nRow;
        }, 
    } );

});
