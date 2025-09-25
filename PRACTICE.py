def rectangle_validator(sideA, sideB, sideC, sideD):
    if sideA == sideC and sideB == sideD:
        print("True")
    else:
        print("False")

def main():
    sideA = float(int(input("Enter side A: ")))
    sideB = float(int(input("Enter side B: ")))
    sideC = float(int(input("Enter side C: ")))
    sideD = float(int(input("Enter side D: ")))
    rectangle_validator(sideA, sideB, sideC, sideD)

main()