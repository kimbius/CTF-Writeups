import pwn
io = pwn.remote("rpca2.rpca.ac.th", 38013)

win_conds = {
    "R": "BYW",

    "B": "YPW",

    "Y": "PGW",

    "P": "GRW",

    "G": "RBW",
}


def get_resp():
    return io.recvline().decode().strip()

while True:
    ply1 = get_resp()
    while len(ply1) != 35:
        print(ply1)
        ply1 = get_resp()
    ply2 = get_resp()
    ply1_score = 0
    ply2_score = 0
    tie = 0
    print(ply1, ply2)
    for card_idx in range(35):
        if ply1[card_idx] in win_conds and ply2[card_idx] in win_conds[ply1[card_idx]]:
            ply1_score += 1
        elif ply2[card_idx] in win_conds and ply1[card_idx] in win_conds[ply2[card_idx]]:
            ply2_score += 1
        else:
            tie += 1
    print(tie, ply1_score, ply2_score)
    state = ply1_score > ply2_score and "1" or "2"
    if tie > 10 or ply1_score == ply2_score:
        state = "0"
    print(f"{state=}")
    io.sendlineafter(b"Who is the winner?", state.encode())