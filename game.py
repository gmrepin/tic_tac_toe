from gameparts import Board, quantiti_check, save_result


game = Board()
game.display()
current_player = 'X'
while True:
    print(f'Ход делает игрок: {current_player}')
    row, column = quantiti_check(game.field_size, game.board)
    game.make_move(row, column, current_player)
    print('Ход сделан!')
    game.display()
    if game.check_winner(current_player):
        message = f'Победили {current_player}!'
        print(message)
        save_result(message)
        break
    elif game.is_board_full():
        message = 'Ничья!'
        print(message)
        save_result(message)
        break
    current_player = 'O' if current_player == 'X' else 'X'
