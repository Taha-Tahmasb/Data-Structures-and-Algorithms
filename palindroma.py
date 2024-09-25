def check_palindrom(tmp:str , s , e):
    if s == e :
        return True 
    if tmp[s] != tmp[e]:
        return False
    if s < e + 1 :
        return check_palindrom(tmp , s + 1 , e - 1 )
def is_palindrom(tmp:str):
    n = len(tmp)
    if n == 0 : 
        return True 
    return check_palindrom(tmp , 0 , n - 1)

n = int(input())
m = str(input())
if is_palindrom(m):
    print("YES")
else :
    print("NO")