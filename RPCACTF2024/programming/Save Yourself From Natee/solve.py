import pwn, re, itertools

solve_steps = 10
challenge_port = 38001

def parse_password(raw_pass_grid):
    return re.findall(r"\d", raw_pass_grid)

rotation_mapping = {
    "A": {
        0: 1,
        1: 4,
        3: 0,
        4: 3
    },
    "B": {
        1: 2,
        2: 5,
        5: 4,
        4: 1
    },
    "C": {
        3: 4,
        4: 7,
        7: 6,
        6: 3
    },
    "D": {
        4: 5,
        5: 8,
        8: 7,
        7: 4
    },
}

def rotate(grid, group):
    rotated_grid = grid.copy()
    for index, target_index in rotation_mapping[group].items():
        rotated_grid[target_index] = grid[index]
    return rotated_grid


class rubix:
    def __init__(self, current_password) -> None:
        self.current_password = current_password
        self.history = []
    
    def rotate(self, group):
        self.current_password = rotate(self.current_password, group)
        self.history.append(group)
        return self.current_password

def possible_village(current_password, correct_password):
    village = itertools.product("ABCD", repeat=solve_steps)
    for group in village:
        obj = rubix(current_password)
        for item in group:
            if obj.rotate(item) == correct_password:
                return obj.history
    return None

io = pwn.remote("rpca2.rpca.ac.th", challenge_port)
io.sendlineafter(b"When you're ready, press X to start surviving game.", b"X")
while True:
    raw_resp = io.recvuntil(b"Keep trying").decode()
    raw_correct_password = raw_resp.split("The correct password is\n\n")[1].split("\n\n")[0].strip()
    raw_current_password = raw_resp.split("Current password is\n\n")[1].split("\n\n")[0].strip()
    correct_password = parse_password(raw_correct_password)
    current_password = parse_password(raw_current_password)
    village = possible_village(
        current_password,
        correct_password
    )
    print(f"{village=}")
    for group in village:
        io.sendlineafter(b"Please enter A B C D :", group.encode())
    result = io.recvline()
    print(f"{result=}")
    b = io.recvlines(5)
    print(f"{b=}")
    if b"Congratulations" in b[-1]:
        io.interactive()
    if b"Correct Password" not in result:
        break