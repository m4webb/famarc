var file_list;
var sort_by;

function get_file_list(callback) {
    $.getJSON('/file_list.json', function(json) {
        file_list = json;
        callback();
    });
}

function sort_id() {
    file_list.sort(function(a,b) {
        if (a.id > b.id) {
            return 1
        } else if (a.id < b.id) {
            return -1
        } else {
            return 0
        }
    });
}

function sort_name() {
    file_list.sort(function(a,b) {
        if (a.name > b.name) {
            return 1
        } else if (a.name < b.name) {
            return -1
        } else {
            return 0
        }
    });
}

function sort_ext() {
    file_list.sort(function(a,b) {
        if (a.ext > b.ext) {
            return 1
        } else if (a.ext < b.ext) {
            return -1
        } else {
            return 0
        }
    });
}

function sort_added() {
    file_list.sort(function(a,b) {
        if (a.added > b.added) {
            return 1
        } else if (a.added < b.added) {
            return -1
        } else {
            return 0
        }
    });
}

function sort_description() {
    file_list.sort(function(a,b) {
        if (a.description > b.description) {
            return 1
        } else if (a.description < b.description) {
            return -1
        } else {
            return 0
        }
    });
}

function draw_file_table_head() {
    var head = $('#file_table > thead');
    head.empty();
    head.append('<tr>' + 
                '<th class="sort_id">Id</th>' + 
                '<th class="sort_name">Name</th>' + 
                '<th class="sort_ext">Ext</th>' + 
                '<th class="sort_added">Added</th>' + 
                '<th class="sort_description">Description</th>' + 
                '</tr>');
    sort_by = head.find(".sort_id");
    sort_by.addClass("emph");
    sort_id();

    head.find(".sort_id").click(function () {
        sort_id(); 
        draw_file_table_body();
        sort_by.removeClass("emph");
        sort_by = $("#file_table > thead .sort_id");
        sort_by.addClass("emph");
    });

    head.find(".sort_name").click(function () {
        sort_name(); 
        draw_file_table_body();
        sort_by.removeClass("emph");
        sort_by = $("#file_table > thead .sort_name");
        sort_by.addClass("emph");
    });

    head.find(".sort_ext").click(function () {
        sort_ext(); 
        draw_file_table_body();
        sort_by.removeClass("emph");
        sort_by = $("#file_table > thead .sort_ext");
        sort_by.addClass("emph");
    });

    head.find(".sort_added").click(function () {
        sort_added(); 
        draw_file_table_body();
        sort_by.removeClass("emph");
        sort_by = $("#file_table > thead .sort_added");
        sort_by.addClass("emph");
    });

    head.find(".sort_description").click(function () {
        sort_description(); 
        draw_file_table_body();
        sort_by.removeClass("emph");
        sort_by = $("#file_table > thead .sort_description");
        sort_by.addClass("emph");
    });

}

function draw_file_table_body() {
    var body = $('#file_table > tbody');
    body.empty();
    $.each(file_list, function (ind, file) {
        var description;
        if (file.description.length > 50) { 
            description = file.description.slice(0,50) + '...';
        } else {
            description = file.description;
        }
            
        body.append('<tr>' + 
                      '<td class=id>' + file.id + '</td>' +
                      '<td>' + file.name + '</td>' +
                      '<td>' + file.ext + '</td>' +
                      '<td>' + file.added + '</td>' + 
                      '<td>' + description + '</td>' + 
                      '</tr>');
    });

    $('#file_table > tbody tr').click( function() {
        window.open('/files/' + $(this).find('.id').html());
    });
}


//on load
$(function() {

    //initialize
    get_file_list(function() {
        draw_file_table_head(); 
        draw_file_table_body();
    });

});
