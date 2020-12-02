valid = 0
invalid = 0
with open("input", "r") as file:
    for row in file.readlines():
        parts = row.split(':')

        password = parts[1][1:]

        ruleParts = parts[0].split(' ')
        ruleRange = ruleParts[0]
        ruleStr = ruleParts[1]

        ruleMin = int(ruleRange.split('-')[0])
        ruleMax = int(ruleRange.split('-')[1])


        if ruleMin <= password.count(ruleStr) <= ruleMax:
            valid += 1
        else:
            invalid += 1

print("VALID: ", valid)
print("INVALID: ", invalid)
print("TOTAL: ", valid + invalid)
