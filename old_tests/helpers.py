def readable_moves(moves):
    return ['pos_yx: ' + str(move['pos']) + 'beated_coins_yx: ' + str([(coin.x, coin.y) for coin in move['beated_coins']]) for move in moves]

def make_beated_coins_from_pos(board, coin):
    print('ok')
    for move in coin.moves['obligatory']:
        all_poses = [(coin.y, coin.x)] + move['pos']
        for i in range(len(move['pos'])):
            print(all_poses[i])
