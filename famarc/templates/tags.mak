<%inherit file="base.mak"/>

<%block name="head">
    <title>Files</title>
    ${parent.head()}
    <link rel="stylesheet" type="text/css" href="/static/tags.css">
    <script src="/static/tags.js"></script>
</%block>

<%block name="content">
    <table id="tags_table">
        <thead>
            <tr>
                <th class="id">Id</th>
                <th>Name</th>
                <th>Description</th>
                <th>Files</th>
            </tr>
        </thead>
        <tbody>
        </tbody>
    </table>
</%block>
