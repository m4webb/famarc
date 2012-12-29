<%inherit file="base.mak"/>

<table>
    % for file in files:
        ${makerow(file)}
    % endfor
</table>

<%def name="makerow(file)">
    <tr>
        <td>${file.name}</td>\
        <td>${file.ext}</td>\
        <td>${file.added}</td>\
    </tr>
</%def>
