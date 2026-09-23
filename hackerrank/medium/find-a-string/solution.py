def mutate_string(string, position, character):
    s = list(string)
    s[position]=character
    s_new = "".join(s)
    return s_new

