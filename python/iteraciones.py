#!/usr/bin/python3

def contador():
    con = 0
    con_interno = 0 

    while con < 10:
        while con_interno < 15:
            print(con, con_interno)
            #con_interno += 1
    con += 1   
    con_interno = 0


if __name__=="__main__":
    contador()
