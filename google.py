def solution(s):
    diameter = len(s)

    for i in range(diameter):
        slices = s.count(s[0:i])
        if (s[0:i] * slices == s):
            string = s[0:i]
            if s[diameter - len(string):diameter] == s[0:i]:
                return slices
    if s == '':
        return 0
    if s[0:i] * slices != s:
        return 1
    
   
print(solution("abcabcabc"))