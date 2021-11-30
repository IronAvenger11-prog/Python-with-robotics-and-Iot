from dorna2 import dorna

def main():
    robot = dorna()
    ip = 'address from the api'
    port = 443
    robot.connect(ip,port)
    print("Connected")

    for i in ramge(10):
        #moving the arm
        robot.play(cmd="lmove",rel=1,z=100*(-1)**(i+1))
        robot.wait(id=i+1,stat=2)
        print("motion",i,"is completed")
        robot.close()

def main_sys():
    robot = dorna()
    ip = 'address from the api'
    port = 443
    robot.connect(ip,port)
    print("Connected")
    
    start = time.time()
    while time.time()-start<10:
        print(robot.sys)


if __name__ == '__main__':
    main()

