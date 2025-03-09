import tkinter as tk
from tkinter import messagebox

# Создание главного окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("400x500")

# Глобальные переменные
current_player = "X"
buttons = []
player_wins = {"X": 0, "O": 0}
game_over = False
total_games = 0

# Функция проверки победителя
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False


# Функция проверки ничьей
def check_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True


# Функция обработки клика по кнопке
def on_click(row, col):
    global current_player, game_over

    if buttons[row][col]['text'] != "" or game_over:
        return

    buttons[row][col]['text'] = current_player

    if check_winner():
        player_wins[current_player] += 1
        update_scoreboard()
        messagebox.showinfo("Игра окончена", f"Игрок {current_player} победил!")
        game_over = True
        check_game_end()
    elif check_draw():
        messagebox.showinfo("Игра окончена", "Ничья!")
        game_over = True
        check_game_end()
    else:
        current_player = "O" if current_player == "X" else "X"


# Функция сброса игры
def reset_game():
    global current_player, game_over
    for row in buttons:
        for btn in row:
            btn["text"] = ""
    current_player = "X" if total_games % 2 == 0 else "O"
    game_over = False


# Функция обновления счетчика побед
def update_scoreboard():
    scoreboard_label.config(text=f"Счет: X - {player_wins['X']} | O - {player_wins['O']}")


# Функция проверки завершения серии игр
def check_game_end():
    global total_games
    if player_wins["X"] == 3:
        messagebox.showinfo("Серия игр окончена", "Игрок X выиграл серию!")
        reset_series()
    elif player_wins["O"] == 3:
        messagebox.showinfo("Серия игр окончена", "Игрок O выиграл серию!")
        reset_series()
    else:
        total_games += 1
        reset_game()


# Функция сброса серии игр
def reset_series():
    global total_games, player_wins
    total_games = 0
    player_wins = {"X": 0, "O": 0}
    update_scoreboard()
    reset_game()


# Создание игрового поля
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            window,
            text="",
            font=("Arial", 20),
            width=6,
            height=3,
            bg="#f0f0f0",
            command=lambda r=i, c=j: on_click(r, c),
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        row.append(btn)
    buttons.append(row)

# Создание интерфейса
scoreboard_label = tk.Label(window, text="Счет: X - 0 | O - 0", font=("Arial", 14), pady=10)
scoreboard_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(window, text="Сбросить игру", font=("Arial", 12), command=reset_game, bg="#ffcccb")
reset_button.grid(row=4, column=0, columnspan=3, pady=10)

reset_series_button = tk.Button(window, text="Сбросить серию", font=("Arial", 12), command=reset_series, bg="#add8e6")
reset_series_button.grid(row=5, column=0, columnspan=3, pady=10)

# Запуск главного цикла
window.mainloop()