valid = 0
invalid = 0
with open("input", "r") as file:
    for row in file.readlines():
        parts = row.split(':')

        password = parts[1][1:]

        ruleParts = parts[0].split(' ')
        ruleRange = ruleParts[0]
        ruleStr = ruleParts[1]

        ruleFirst = int(ruleRange.split('-')[0])
        ruleSecond = int(ruleRange.split('-')[1])

        match = 0
        if password[ruleFirst-1] == ruleStr:
            match += 1
        if password[ruleSecond-1] == ruleStr:
            match += 1

        if match == 1:
            valid += 1
        else:
            invalid += 1

print("VALID: ", valid)
print("INVALID: ", invalid)
print("TOTAL: ", valid + invalid)
