pip install kociemba
import kociemba

def solve_rubiks_cube(cube_string):
    """
    Solves the Rubik's Cube using the Kociemba's algorithm.

    Parameters:
    cube_string (str): A string representing the current state of the Rubik's Cube.

    Returns:
    str: The solution as a series of moves.
    """
    try:
        solution = kociemba.solve(cube_string)
        return solution
    except ValueError as e:
        return f"Error: {e}. Please ensure the cube string is valid."

# Example usage
if __name__ == "__main__":
    # Example scrambled cube in Kociemba notation
    scrambled_cube = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"

    print("Scrambled Cube State:")
    print(scrambled_cube)

    print("\nSolving the Cube...")
    solution = solve_rubiks_cube(scrambled_cube)
    print("Solution:")
    print(solution)
import random

def scramble_cube():
    moves = ["U", "R", "F", "D", "L", "B", "U'", "R'", "F'", "D'", "L'", "B'", "U2", "R2", "F2", "D2", "L2", "B2"]
    scramble = " ".join(random.choices(moves, k=25))
    return scramble
