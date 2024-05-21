~~~ Notes de Hanoi ~~~

Main |:
    src <- {C4 D4 E4 F4 G4}
    <!> "list len is" #src "last element is" src[#src]
    dst <- {}
    aux <- {}
    HanoiRec #src src dst aux
:|

HanoiRec n src dst aux |:
    if n > 0 |:
        HanoiRec (n - 1) src aux dst
        note <- src[#src]
        8< src[#src]
        dst << note
        <:> note
        HanoiRec (n - 1) aux dst src
    :|
:|