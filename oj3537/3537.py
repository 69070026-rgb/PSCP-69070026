"""Impostor"""
import ast
def main():
    """Impostor"""
    players = {}
    dead = {}
    while True:
        info = input()
        if info == "Start":
            break
        players.update(ast.literal_eval(info))
    while True:
        out = input()
        if out == "End":
            break
        if out in players:
            dead[out] = players[out]
            del players[out]
    impostor = list(players.values()).count("Impostor")
    print(f"{impostor} Impostor Remains")
    print("***Alive***")
    for key in sorted(players.keys()):
        print(f"{key} : {players[key]}")
    print("***Dead***")
    for key in sorted(dead.keys()):
        print(f"{key} : {dead[key]}")
main()
