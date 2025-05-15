def create_multiplication_table():
    table = []
    for i in range(1, 6): 
        row = []
        for j in range(1, 11): 
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        print(" ".join(str(num).rjust(2) for num in row))
