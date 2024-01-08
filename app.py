import chess
from chess.pgn import read_game
from io import StringIO
import time
import os

def pgn_to_ascii(pgn_code, max_moves=550): #for now the moves are taken as 1 move per piece but in chess 1 is move is consider when both side pieces are moved
    pgn_code = '\n'.join(line.strip() for line in pgn_code.strip().split('\n'))
    pgn_file = StringIO(pgn_code)
    game = read_game(pgn_file)
    board = chess.Board()

    for move_number, move in enumerate(game.mainline_moves(), 1):
        if move_number > max_moves:
            break

        board.push(move)
        os.system("clear" if os.name == "posix" else "cls")  # Clear the console
        print(board)
        time.sleep(1)  # Add a delay to make moves visible, adjust as needed

if __name__ == "__main__":
    # Example PGN chess code
    example_pgn = """
    1. e4 e5
    2. Nf3 Nc6
    3. Bb5 a6
    4. Ba4 Nf6
    5. O-O Be7
    6. Re1 b5
    7. Bb3 d6
    8. c3 O-O
    9. h3 Nb8
    10. d4 Nbd7
    11. Nbd2 Bb7
    12. Bc2 Re8
    13. Nf1 Bf8
    14. Ng3 g6
    15. a4 Bg7
    16. Bg5 h6
    17. Bd2 c5
    18. d5 c4
    19. Be3 Qc7
    20. Qd2 h5
    21. Bh6 Bh8
    22. Nh4 Nc5
    23. Rf1 bxa4
    24. f4 exf4
    25. Qxf4 Re5
    26. Nf3 Ree8
    27. Bg5 Nh7
    28. Bh6 Qe7
    29. h4 Bc8
    30. Rae1 Bd7
    31. Re3 Bg7
    32. Bxg7 Kxg7
    33. Nd4 Nf8
    34. Ref3 Kg8
    35. Qxf7+ Qxf7
    36. Rxf7 Rad8
    37. R7f6 Bc8
    38. Nc6 Rd7
    39. e5 dxe5
    40. Bxg6 Nxg6
    41. Rxg6+ Rg7
    42. Rxg7+ Kxg7
    43. Nxh5+ Kg6
    44. Nf6 Rh8
    45. Nxe5+ Kg7
    46. h5 Rh6
    47. Ne8+ Kg8
    48. g4 Bxg4
    49. Nxg4 Rb6
    50. d6 Rxb2
    51. h6 Rb7
    52. Nef6+ Kh8
    53. Ne5 Ne6
    54. d7 Rxd7
    55. Nexd7 a3
    56. Ne5 Ng5
    57. Rf5 a2
    58. Rxg5 a1=Q+
    59. Kg2 Qb2+
    60. Kh1 Qc1+
    61. Rg1 Qxg1+
    62. Kxg1 a5
    63. Nf7#
    """

    pgn_to_ascii(example_pgn)
