# def move_rings(n, s, e, b):
#        if n == 0:
#            print e
#            return
#        b = s.pop(0)
#        e.append(b)
#        move_rings(len(s), s, e, b)

def move_rings(n, s, e, b):
    if n == 1:
        e.append(s.pop(0))
        return
    move_rings(n - 1, s, b, e)
    e.append(s.pop(0))
    move_rings(n-1, b, e, s)
       
print move_rings(5, [4,3,2,1,0], [], [])

