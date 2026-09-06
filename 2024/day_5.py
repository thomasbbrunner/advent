from pathlib import Path

if __name__ == "__main__":
    data = Path("./2024/day_5.txt").read_text()

    deps: dict[int, set[int]] = {}
    seqs: list[tuple[int, ...]] = []
    is_deps = True
    for line in data.splitlines():
        if line == "\n" or not line:
            is_deps = False
            continue
        
        if is_deps:
            vals = line.split("|")

            val_ref, val = int(vals[0]), int(vals[1])
            
            if val_ref not in deps:
                deps[int(val_ref)] = set()
            deps[int(val_ref)].add(int(val))
        
        else:
            seqs.append(tuple(int(val) for val in line.split(",")))

    valids: list[bool] = [True for _ in range(len(seqs))]
    for seq_idx, seq in enumerate(seqs):
        for idx, val_ref in enumerate(reversed(seq)):
            sub_set = set(seq[-idx-2::-1])
            if sub_set & deps.get(val_ref, set()):
                valids[seq_idx] = False

    res = 0
    for idx, valid in enumerate(valids):
        if not valid: continue

        seq = seqs[idx]
        res += seq[len(seq)//2]

    print(res)

    seqs_sorted: list[tuple[int, ...]] = []
    for seq_idx, valid in enumerate(valids):
        if valid: continue

        seq = seqs[seq_idx]
        deps_seq = {val_ref: [val for val in vals if val in seq] for val_ref, vals in deps.items() if val_ref in seq}
        orfans = [val for val in seq if len(deps_seq[val]) == 0]

        seq_sorted = []
        while orfans:
            orfan = orfans.pop()
            seq_sorted.append(orfan)
            deps_seq.pop(orfan)

            for val_ref in deps_seq:
                if orfan in deps_seq[val_ref]:
                    deps_seq[val_ref].remove(orfan)
            
            for val_ref in deps_seq:
                if len(deps_seq[val_ref]) == 0:
                    orfans.append(val_ref)
                    break
        
        seqs_sorted.append(seq_sorted)
        
    res = 0
    for seq in seqs_sorted:
        res += seq[len(seq)//2]

    print(res)