<%inherit file="base.mak"/>

<%block name="head">
    <title>Files</title>
    ${parent.head()}
    <link rel="stylesheet" type="text/css" href="/static/files.css">
    <script src="/static/files.js"></script>
</%block>

<%block name="content">
    <table id="file_table">
        <thead>
            <tr>
                <th class="id">Id</th>
                <th>Name</th>
                <th>Ext</th>
                <th>Added</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
</%block>
