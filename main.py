import sys
# Minimal chess engine logic
def move(board):
    return list(board.legal_moves)[0]
if __name__ == "__main__":
    print("Chess Engine Ready")
