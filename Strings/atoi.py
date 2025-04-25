def myAtoi(s):
    # Step 1: Initialize variables
    sign = 1          # To track positive or negative sign
    res = 0           # To store the result
    idx = 0           # Pointer to iterate through the string

    # Step 2: Skip leading whitespaces
    while idx < len(s) and s[idx] == ' ':
        idx += 1

    # Step 3: Check for optional '+' or '-' sign
    if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
        if s[idx] == '-':
            sign = -1
        idx += 1

    # Step 4: Convert digits to integer
    while idx < len(s) and '0' <= s[idx] <= '9':
        # Use ord to convert character to integer
        res = 10 * res + (ord(s[idx]) - ord('0'))

        # Step 5: Clamp result to 32-bit signed integer range
        if res > (2**31 - 1):
            return sign * (2**31 - 1) if sign == 1 else -2**31
        
        idx += 1

    # Step 6: Apply sign and return final result
    return res * sign

print(type(myAtoi('-12342343')))