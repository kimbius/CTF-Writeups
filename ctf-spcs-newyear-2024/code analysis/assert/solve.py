from sympy import symbols, Eq, solve

a, b, c, d, e, f, g, h, i = symbols('a b c d e f g h i')
eq1 = Eq(b, c)
eq2 = Eq(c, g)
eq3 = Eq(g, h)
eq4 = Eq(g + b + c, 0)
eq5 = Eq(3 * a + 12 * d + e + 4 * f + 6 * i, 2194)
eq6 = Eq(-6 * a + 2 * d - 4 * e - f + 9 * i, -243)
eq7 = Eq(a + 6 * d + 2 * e + 7 * f + 11 * i, 2307)
eq8 = Eq(5 * a - 2 * d - 7 * e + 76 * f + 8 * i, 8238)
eq9 = Eq(2 * a - 2 * d - 2 * e - 2 * f + 2 * i, -72)

solution = solve((eq1, eq2, eq3, eq4, eq5, eq6, eq7, eq8, eq9), (a, b, c, d, e, f, g, h, i))
print(f"{solution=}")

a, b, c, d, e, f, g, h, i = map(lambda x: x[1], solution.items())

def xorc(a, b):
    return chr(ord(a) ^ ord(b))

def xorstr(a, b):
    return ('').join([ xorc(a[(i % len(a))], c) for i, c in enumerate(b) ])

codestr = ('').join(chr(x) for x in [a, b, c, d, e, f, g, h, i])
result = xorstr(codestr, '\x1bro#&\x0b{t;\x19_44;Wrt\x0cLp35|\x100r\x0c\x15s_1{\x16y_&\x0f3f2$;wh`\x12_dt*\x11gg:\x12g_7:Tgrg\x11s}')
print(result) # grodno{the_4ss3rt_0p3r4t0r_is_v3ry_us3ful_wh3n_d3bugging_pr0gr4ms}