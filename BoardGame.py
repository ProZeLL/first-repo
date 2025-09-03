# Function untuk menggambar papan permainan
def print_game_board(size, board_dict):
    for i in range(size):
        row = []
        for j in range(size):
            pos = i * size + j  # Hitung posisi dalam dictionary
            if pos in board_dict:
                symbols = board_dict[pos]  # Ambil simbol dari dictionary
                if len(symbols) == 0:
                    row.append("  ")  # Jika kosong, tambahkan dua spasi
                elif len(symbols) == 1:
                    row.append(" %s" % symbols[0])  # Satu simbol, tampilkan di tengah
                else:
                    row.append(" %s" % symbols[-len(symbols):])  # Banyak simbol, tampilkan di kanan
            else:
                row.append("  ")  # Jika tidak ada, tambahkan dua spasi

        print("|".join(row))  # Gabungkan baris dengan |
        if i < size - 1:
            print("---|---|---")  # Cetak garis pemisah antara baris


# Function untuk dictionary game board 1
def GameBoard_1():
    dictionary = {0: [], 1: [], 2: [],
                  3: [], 4: [], 5: [],
                  6: [], 7: [], 8: []}
    print("Game Board - 1")
    print_game_board(3, dictionary)


# Function untuk dictionary game board 2
def GameBoard_2():
    dictionary = {0: ["A"], 1: ["B"], 2: ["C"],
                  3: ["B"], 4: [], 5: ["C"],
                  6: ["B"], 7: ["D"], 8: []}
    print("Game Board - 2")
    print_game_board(3, dictionary)


# Function untuk dictionary game board 3
def GameBoard_3():
    dictionary = {0: ["A"],
                  1: ["B", "C"],
                  2: ["C", "D"],
                  3: [],
                  4: ["B"],
                  5: ["B", "C"],
                  6: ["A", "A"],
                  7: ["B", "B"],
                  8: ["C"],
                  9: ["D", "A"]}
    print("Game Board - 3")
    print_game_board(3, dictionary)


# Function untuk dictionary game board 4
def GameBoard_4():
    dictionary = {0: ["A", "B", "C"],
                  1: ["B", "C", "B"],
                  2: ["C", "D", "A"],
                  3: ["D", "A"],
                  4: ["B", "C"],
                  5: [],
                  6: ["A", "A"],
                  7: ["B", "B", "D"],
                  8: ["D", "C"],
                  9: ["D", "A"]}
    print("Game Board - 4")
    print_game_board(3, dictionary)


# Tampilkan masing-masing dari keempat desain game board tersebut
GameBoard_1()
print()  # Baris kosong antara papan
GameBoard_2()
print()  # Baris kosong antara papan
GameBoard_3()
print()  # Baris kosong antara papan
GameBoard_4()
