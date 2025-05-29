# code for my thingy
#connect pins to the different things
calculating = False
value = 0
score1 = 8000
score2 = 8000
one = False
#code plus or minus button to enter the mode and then for the enter thing
if(push and not calculating):
    calculating = True
    mode = "s"
elif(push and calculating):
    solve(value, False)
if(push2 and not calculating):
    calculating = True
    mode = "p"
elif(push2 and calculating):
    solve(value, False)

if(switch1):
    one = True
else:
    one = False
#code the maliss button to decrease by 300
if(push3):
    solve(-300, False)
#code the half to divide by two or if in equasion clear
if(push4 and not calculating):
    solve(value, True)
elif(push4 and calculating):
    value = "0"
#code each number to but that into the equasion
if(push5 and calculating):
    value = (value + "9")
if(push6 and calculating):
    value = (value + "8")
if(push7 and calculating):
    value = (value + "7")
if(push8 and calculating):
    value = (value + "6")
if(push9 and calculating):
    value = (value + "5")
if(push10 and calculating):
    value = (value + "4")
if(push11 and calculating):
    value = (value + "3")
if(push12 and calculating):
    value = (value + "2")
if(push13 and calculating):
    value = (value + "1")
if(push14 and calculating):
    value = (value + "0")
if(push15 and calculating):
    value = (value + "00")
if(push16 and calculating):
    value = (value + "000")

def solve(m, t):
    if(not t):
        if(one):
            score1 += int(m)
        else:
            score2 += int(m)
    else:
        if(one):
            score1/2
        else:
            score2/2
    value = "0"