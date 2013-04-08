<%inherit file="base.mak"/>

<%block name="head">
    <title>Files</title>
    ${parent.head()}
    <link rel="stylesheet" type="text/css" href="/static/files_base.css">
    <script src="/static/files_base.js"></script>
</%block>

<%block name="content">
    <table id="file_description">
        <thead>
        </thead>
        <tbody>
            <tr>
                <td>File</td>
                <td>${file.id}</td> 
            </tr>
            <tr>
                <td>Name</td>
                <td>${file.name}.${file.ext}</td> 
            </tr>
            <tr>
                <td>Description</td>
                <td>${file.description}</td> 
            </tr>
            <tr>
                <td>Added</td>
                <td>${file.added}</td> 
            </tr>
        </tbody>
    </table>
    <table id="file_tags">
        <thead>
            <tr>
                <th>Tags</td>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
    <form id="tag_form">
        <input id="newtag" name="tag" type="text" />
    </form>
    <a href="/files/${file.id}/view">View</a>
    <a href="/files/${file.id}/download">Download</a>
</%block>
