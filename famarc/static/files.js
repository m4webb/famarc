//on load
$(function() {

    //$('#example').dataTable( {
    //    "bProcessing" : true,
    //    "sAjaxSource" : "/file_table.json",
    //    "sDom" : 'ftr',
    //    "sScrollY": "400px", 
    //    "bPaginate": false,
    //    "aoColumnDefs": [
    //          { "sClass": "id", 
    //            "aTargets": [ "id" ] 
    //          }
    //        ],
    //    "fnCreatedRow": function( nRow, aData, iDataIndex ) {
    //        $(nRow).click( function() {
    //            window.open('/files/' + $(nRow).find('.id').html(), "_self");
    //        });
    //        //$('td', nRow).attr('nowrap', 'nowrap');
    //        return nRow;
    //    }, 
    //} );

    $('#file_table').dataTable( {
        "bProcessing": true,
        "bServerSide": true,
        "sAjaxSource": "files/@@data.json",
        "fnServerData": function ( sSource, aoData, fnCallback, oSettings ) {
            oSettings.jqXHR = $.ajax( {
                "dataType": 'json',
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": fnCallback
            } );
        }
    } );

});
