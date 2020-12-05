import re

with open("input", "r") as input:
    passports = [
        {entry[0]:entry[1] for entry in list(
            map(
                lambda field: field.split(':'),
                line.replace('\n', ' ').split(' ')
            )
        )} for line in input.read().split('\n\n')
    ]

valid = 0
invalid = 0
for passport in passports:
    if len(passport.keys()) == 8:
        valid += 1
    elif len(passport.keys()) == 7 and not 'cid' in passport.keys():
        valid += 1
    else:
        invalid += 1

print('PART ONE')
print('\tVALID: ', valid)
print('\tINVALID: ', invalid)
print('\tTOTAL: ', valid + invalid)

def validateFields(passport):
    # Birth Year - four digits; at least 1920 and at most 2002
    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    # Issue Year - four digits; at least 2010 and at most 2020
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    # Expiration Year - four digits; at least 2020 and at most 2030
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    # Height - a number followed by either cm or in
    if not (passport['hgt'][-2:] in ['cm', 'in']):
        return False
    else:
        # cm - at least 150 and at most 193
        if passport['hgt'][-2:] == 'cm' and not (150 <= int(passport['hgt'][:-2]) <= 193):
            return False
        # in - at least 59 and at most 76
        if passport['hgt'][-2:] == 'in' and not (59 <= int(passport['hgt'][:-2]) <= 76):
            return False
    # Hair Color - # followed by exactly six characters 0-9 or a-f
    if not re.search('^#[a-f0-9]{6}$', passport['hcl']):
        return False
    # Eye Color - exactly one of: amb blu brn gry grn hzl oth
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    # Passport ID - a nine-digit number, including leading zeroes
    if not re.search('^[0-9]{9}$', passport['pid']):
        return False
    return True

valid = 0
invalid = 0
for passport in passports:
    if len(passport.keys()) == 8 and validateFields(passport):
        #print('PASS:')
        #print('\tbyr', passport['byr'])
        #print('\tiyr', passport['iyr'])
        #print('\teyr', passport['eyr'])
        #print('\thgt', passport['hgt'])
        #print('\thcl', passport['hcl'])
        #print('\tecl', passport['ecl'])
        #print('\tpid', passport['pid'])
        #print('\tcid', passport['cid'])
        valid += 1
    elif len(passport.keys()) == 7 and (not 'cid' in passport.keys()) and validateFields(passport):
        #print('PASS:')
        #print('\tbyr', passport['byr'])
        #print('\tiyr', passport['iyr'])
        #print('\teyr', passport['eyr'])
        #print('\thgt', passport['hgt'])
        #print('\thcl', passport['hcl'])
        #print('\tecl', passport['ecl'])
        #print('\tpid', passport['pid'])
        valid += 1
    else:
        invalid += 1

print('PART TWO')
print('\tVALID: ', valid)
print('\tINVALID: ', invalid)
print('\tTOTAL: ', valid + invalid)
