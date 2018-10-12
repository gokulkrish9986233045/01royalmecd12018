a=['1','2','3','4','5','6','7','8','9']

def print_board():
    print(a[0],'|',a[1],'|',a[2])
    print("----------")
    print(a[3],'|',a[4],'|',a[5])
    print("----------")
    print(a[6],'|',a[7],'|',a[8])
     
playeroneturn = True
while True:
	print_board()
	p=input("choose an available place : ")

	if(p in a):
        if(a[int(p)-1]=='x' or a[int(p)-1]=='o'):
            print("place taken, choose another place")
         	continue
        else:
         	if playeroneturn:
         		a[int(p)-1]='X'
         	    playeroneturn=not playeroneturn
            else:
         	    a [int(p)-1]='o'
         	    playeroneturn=not playeroneturn
            for i in(0,3,6):


