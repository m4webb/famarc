<html>

<head>
<%block name="head">
    <link rel="stylesheet" type="text/css" href="/static/base.css">
    <script src="/static/jquery.js"></script>
    <script src="/static/jquery.dataTables.min.js"></script>
</%block>
</head>

<body>
<div id="container">

<div id="header">
    <ul id="nav">
        <li id="navhome"><a href="/">Home</a></li>
        <li><a href="/people" target="_blank">People</a></li>
        <li><a href="/places">Places</a></li>
        <li><a href="/files">Files</a></li>
        <li><a href="/tags">Tags</a></li>
    </ul>
</div>

<div id="content">
<%block name="content"/>
</div>

<div id="footer">
<%block name="footer"/>
</div>

</div>
</body>

</html>
