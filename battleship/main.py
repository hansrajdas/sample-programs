import battleship

def main():
    p1 = battleship.Player('p1')
    p2 = battleship.Player('p2')

    game = battleship.Battleship()

    print('Game is initialised')
    while True:
        i, j = p1.take_input()
        game.fire(p1, p2, i, j)

        if p2.check_all_ships_down():
            print(f'{p2.name!r} wins')
            break
        p1, p2 = p2, p1

if __name__ == '__main__':
    main()
