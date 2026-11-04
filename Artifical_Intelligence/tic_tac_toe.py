import streamlit as st
import numpy as np
import random


# ---------------------------------------
# Create Board
# ---------------------------------------

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "message" not in st.session_state:
    st.session_state.message = "Player 1's turn"


# ---------------------------------------
# Check Game Status
# ---------------------------------------

def check_status(board):

    # Check rows and columns
    for i in range(3):

        # Row
        if board[i][0] != 0:
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]

        # Column
        if board[0][i] != 0:
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

    # Check first diagonal
    if board[0][0] != 0:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]

    # Check second diagonal
    if board[0][2] != 0:
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

    # Check draw
    if not np.any(board == 0):
        return 3

    # Game still running
    return 0


# ---------------------------------------
# AI Move
# ---------------------------------------

def ai_move():

    board = st.session_state.board

    empty_cells = []

    # Find empty cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                empty_cells.append((i, j))

    # Select random empty cell
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2


# ---------------------------------------
# Restart Game
# ---------------------------------------

if st.button("Restart Game"):

    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.game_over = False
    st.session_state.message = "Player 1's turn"

    st.rerun()


# ---------------------------------------
# Title
# ---------------------------------------

st.title("Tic-Tac-Toe")

st.write("You = X")
st.write("Computer = O")


# ---------------------------------------
# Display Board
# ---------------------------------------

board = st.session_state.board

for i in range(3):

    cols = st.columns(3)

    for j in range(3):

        with cols[j]:

            if board[i][j] == 0:
                symbol = " "

            elif board[i][j] == 1:
                symbol = "X"

            else:
                symbol = "O"

            # Button
            if st.button(
                symbol,
                key=f"cell_{i}_{j}",
                disabled=(
                    board[i][j] != 0
                    or st.session_state.game_over
                )
            ):

                # Human move
                board[i][j] = 1

                # Check human result
                result = check_status(board)

                if result == 1:
                    st.session_state.message = "Player 1 wins!"
                    st.balloons()
                    st.session_state.game_over = True

                elif result == 3:
                    st.session_state.message = "Game Draw!"
                    st.session_state.game_over = True

                else:
                    # Computer move
                    ai_move()

                    # Check computer result
                    result = check_status(board)

                    if result == 2:
                        st.session_state.message = "Computer wins!"
                        st.badge('Game Over',color='red')
                        st.session_state.game_over = True

                    elif result == 3:
                        st.session_state.message = "Game Draw!"
                        st.session_state.game_over = True

                    else:
                        st.session_state.message = "Player 1's turn"

                st.rerun()


# ---------------------------------------
# Game Status
# ---------------------------------------

st.subheader(st.session_state.message)