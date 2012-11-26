var file_list;
var sort_by;

function get_file_list(callback) {
    $.getJSON('/file_list.json', function(json) {
        file_list = json;
        callback();
    });
}

function sort_name() {
    file_list.sort(function(a,b) {
        return a.name < b.name
    });
}

function sort_ext() {
    file_list.sort(function(a,b) {
        return a.ext < b.ext
    });
}

function sort_added() {
    file_list.sort(function(a,b) {
        return a.added < b.added
    });
}

function sort_description() {
    file_list.sort(function(a,b) {
        return a.description > b.description
    });
}

function draw_file_table_head() {
    var head = $('#file_table > thead');
    head.empty();
    head.append('<tr>' + 
                '<th class="sort_name">Name</th>' + 
                '<th class="sort_ext">Ext</th>' + 
                '<th class="sort_added">Added</th>' + 
                '<th class="sort_description">Description</th>' + 
                '</tr>');
    sort_by = head.find(".sort_name");
    sort_by.addClass("emph");
    sort_name();

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
        body.append('<tr>' + 
                      '<td>' + file.name + '</td>' +
                      '<td>' + file.ext + '</td>' +
                      '<td>' + file.added + '</td>' + 
                      '<td>' + file.description + '</td>' + 
                      '</tr>');
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
