# def route___move():
#     try:
#         pawn_move = receive_pawn_move(test_pawn_move)
#         checkers2 = Checkers(State(session['board_state']))
#         if not checkers.pawn_move_is_valid(**pawn_move): raise InvalidPawnMove('No such pawn or move for pawn')
#         checkers.make_move(**pawn_move)
#     except EmptyPawnMove:
#         print('EmptyPawnMove')
#         pass
#     except InvalidPawnMove:
#         """Handle some error"""
#         print('invalidPawnMove Error')
