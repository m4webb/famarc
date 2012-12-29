<%inherit file="base.mak"/>

<%block name="content">
    <form action="/file_write" method="post" accept-charset="utf-8"
          enctype="multipart/form-data">

        <label for="file">File</label>
        <input id="file" name="file" type="file" value="" />
        <input id="file_desc" name="description" type="text" />

        <input type="submit" value="submit" />
    </form>
</%block>
