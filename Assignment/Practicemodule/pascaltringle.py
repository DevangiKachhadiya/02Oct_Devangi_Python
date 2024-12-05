n=int(input("Enter Number of Row:  "))

for i in range(n):
    row=[1]
    if i > 0:
        for j in range(1,i):
            row.append(prev_row[j-1]+prev_row[j])
        row.append(1)
    print(row)
    prev_row=row 