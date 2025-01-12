YesNO=input("Do you want to shut down: ")
def shutdown(ANS="yes"):
    if ANS=="yes":
        print("Shuting down")
    elif ANS=="no":
        print("Shuting down aborted")
    else:
        print("please type yes or no")

shutdown(YesNO)