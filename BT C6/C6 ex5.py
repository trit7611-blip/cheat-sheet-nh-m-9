str = 'X-DSPAM-Confidence:0.8475'
colon_pos = str.find(':')
number_str = str[colon_pos + 1 :]
value = float(number_str)
print(value)