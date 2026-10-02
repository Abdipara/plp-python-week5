import math

def tables_needed(people, seats):
    return math.ceil(people / seats)  # Calculates tables rounded UP

def welcome(name):
    return f"Welcome to PLP, {name}!"  # Returns welcome message

if __name__ == "__main__":
    print(tables_needed(10, 4))