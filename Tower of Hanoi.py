# Tower of Hanoi Program

from TOH_optimalmove_calculator import toh_movecount


def toh(no, s, a, t):
    if no <= 1:
        print(f"Move disk 1 from {s} to {t}")
    else:
        toh(no - 1, s, t, a)
        print(f"Move disk {no} from {s} to {t}")
        toh(no-1, a, s, t)


n = int(input("Enter no. of disks: "))
toh(n, "S", "A", "T")
moves = toh_movecount(n)
print(f"No. of moves: {moves}")
