%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<hr/>
Model List View 
<hr/>
<p>The open items are as follows:</p>
<table border="1">
%for row in rows:
	<tr>
	<td>#{{row[0]}}</td>
	<td><a href="/edit/{{row[0]}}">{{row[1]}}</a></td>
	<td><a href="/edit/{{row[0]}}">{{row[2]}}</a></td>
	<td><a href="/delete/{{row[0]}}"><img src="/static/trash.png" style="width:16px;height:16px;border:0;"/></a></td>
	</tr>
%end
</table>
<hr/>
<p>Enter a new item...</p><br/>
<form action="/new" method="post">
	To be done: <input name="task" type="text" />
	<input value="Save new item..." type="submit" />
</form>
