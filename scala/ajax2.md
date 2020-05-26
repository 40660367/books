# ajax test

<script>
function loadXMLDoc()
{
	var xmlhttp;
	if (window.XMLHttpRequest)
	{
		//  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
		xmlhttp=new XMLHttpRequest();
	}
	else
	{
		// IE6, IE5 浏览器执行代码
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
			document.getElementById("myDiv123").innerHTML=xmlhttp.responseText;
		}
	}
	xmlhttp.open("GET","./images/1.txt",true);
	xmlhttp.send();
}
</script>

<div id="myDiv123">文件名:</div>
<div>
<button type="button" onclick="loadXMLDoc()">修改内容</button>
</div>

