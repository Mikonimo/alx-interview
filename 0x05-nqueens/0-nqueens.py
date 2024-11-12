#!/usr/bin/python3
"""This module contains a function"""
import sys


def is_valid(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    for r, c in board:
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """
    Use backtracking to find all solutions for the N-Queens problem.
    """
    if row == n:
        solutions.append(board.copy())
        return

    for col in range(n):
        if is_valid(board, row, col):
            board.append([row, col])
            solve_nqueens(n, row + 1, board, solutions)
            board.pop()


def nqueens(n):
    """
    Solves the N-Queens problem for a given n and prints all solutions.
    """
    solutions = []
    solve_nqueens(n, 0, [], solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
