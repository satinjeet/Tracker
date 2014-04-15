$(document).ready(function(){
    getCookie = function(key) {
        if (document.cookie.length > 0) {
            k = document.cookie;
            upto = k.indexOf(";")
            if (upto === -1) {
                t = k.substring(k.indexOf(key + "=")).split("=")    
            } else {
                t = k.substring(k.indexOf(key + "="), upto).split("=")
            }
            return t[1];
        } else {
            return ""
        }
    }
    
    setTimeout(function() {
        cookieName = "tkDat"
        var pathname = window.location.pathname;
        cookieData = {}
        try {
            cookieData = JSON.parse(unescape(getCookie(cookieName)));
        } catch (err) {
            console.log (err)
            cookieData = {};
            key = Math.random().toString(36).slice(2);
            cookieData["key"] = key;
            cookieData["data"] = {};
        }

        
        if (cookieData['data'][pathname] == undefined) {
            cookieData['data'][pathname] = 1;
        } else {
            cookieData['data'][pathname] += 1;
        }

        dt = escape(JSON.stringify(cookieData));
        kk = cookieName + "=" + dt;
        document.cookie = kk;

        string = unescape(dt);
        url = "http://localhost:8080/tracker?data=" + string;
        type = "POST";
        var xmlhttp= new XMLHttpRequest();
        xmlhttp.open(type,url,false);
        xmlhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
        xmlhttp.onreadystatechange = function() {
            if (xmlhttp.readyState==4 && xmlhttp.status==200)
            {
                $("#data-cookie").html(string);
            }
        }
        xmlhttp.send();
    }, 3000);
    
});