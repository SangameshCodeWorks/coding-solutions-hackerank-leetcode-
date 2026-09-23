def count_substring(string, sub_string):
    count = 0
    for i in range(0,len(string)):
        s2=string[i:i+len(sub_string)]
        if s2==sub_string:
            count=count+1
        else:
            count=count+0
    return count
            

