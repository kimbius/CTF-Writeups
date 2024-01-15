# rev/CSS Password

### Description
```
My web developer friend said JavaScript is insecure so he made a password vault with CSS. Can you find the password to open the vault?

Wrap the flag in uoftctf{}

Make sure to use a browser that supports the CSS :has selector, such as Firefox 121+ or Chrome 105+. The challenge is verified to work for Firefox 121.0.

Author: notnotpuns
```

```js
let styleSrc = document.head.getElementsByTagName("style")[0].innerHTML
styleSrc.match(/(b\d+_\d+_l\d+_c\d+)/g).map(_ => _.split("_").map(_ => +_.match(/\d+/g)[0])).map(([byte, latch, led, checker]) => {
    let true_key = (
            styleSrc.split(`.wrapper:has(.byte:nth-child(${byte}) .latch:nth-child(${latch}) .latch__reset:active) .checker:nth-of-type(${led+1}) .checker__state:nth-child(${checker})`)[1].split("{")[1].split("}")[0].includes("100%")
    ) ? "reset" : "set"
    return document.body.querySelector(`.byte:nth-child(${byte}) .latch:nth-child(${latch}) .latch__${true_key}`).style.background = "#000"
})

let flag = [...document.querySelectorAll(".byte")].map(byte => [...byte.querySelectorAll(".latch")].map(latch => latch.querySelector(".latch__set").style.background != "" ? 1 : 0).join("")).map(bin => String.fromCharCode(parseInt(bin, 2))).join("")

console.log(`uoftctf{${flag}}`)
```

**Don't bully my coding, please.** 😟