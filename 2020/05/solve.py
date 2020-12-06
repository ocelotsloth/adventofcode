
with open("input", "r") as file:
    lines = [line.strip() for line in file.readlines()]

def processBoardingPass(boardingPass):
    row = 0
    for i in range(7):
        row += int((boardingPass[i] == 'B') * 64 * (0.5 ** i))
    col = 0
    for i in range(3):
        col += int((boardingPass[i + 7] == 'R') * 4 * (0.5 ** i))
    return row * 8 + col

def test_processBoardingPass():
    for test in [('BFFFBBFRRR', 567), ('FFFBBBFRRR', 119), ('BBFFBBFRLL', 820)]:
        result = processBoardingPass(test[0])
        if result != test[1]:
            print('ERROR, ', test[0], 'expected ', test[1], '; got ', result)
            return False
    return True

if test_processBoardingPass():
    seatIDs = sorted([processBoardingPass(boardingPass) for boardingPass in lines])
    print('P1 SOLUTION: ', max(seatIDs))
    for i in range(len(seatIDs)):
        if i == 0 or i == len(seatIDs):
            continue
        if seatIDs[i] - 1 != seatIDs[i - 1]:
            print('P2 SOLUTION: ', seatIDs[i] - 1)
            break
    else:
        print('P2 SOLUTION NOT FOUND')
else:
    print('TESTS FAILED')

