s = input()
ans = 0
match s:
    case 'A+':
        ans = 4.0
    case 'A':
        ans = 3.7
    case 'A-':
        ans = 3.3
    case 'B+':
        ans = 3.0
    case 'B':
        ans = 2.7
    case 'B-':
        ans = 2.3
    case 'C+':
        ans = 2.0
    case 'C':
        ans = 4.0
    case 'C-':
        ans = 1.7
    case 'D+':
        ans = 1.3
    case 'D':
        ans = 1.0
    case 'F':
        ans = 0
print(ans)