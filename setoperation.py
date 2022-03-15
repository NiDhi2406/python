vowels = 'aeiou'
string = 'Hello, have you tried our tutorial section yet?'
string = string.casefold()
count = {}.fromkeys(vowels, 0)
for char in string:
    if char in count:
        count[char] += 1
print(count)

##### other option ######
string = 'Hello, just enjoy and chill your life?'
string = string.casefold()
count = {x : sum([1 for char in string if char == x]) for x in 'aeiou'}
print(count)