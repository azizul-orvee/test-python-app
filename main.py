from circle import calculate_circle_area
from rectangle import calculate_rectangle_area

def main():
    print("Welcome to the Fancy Area Calculator!")
    print("1. Calculate Circle Area")
    print("2. Calculate Rectangle Area")
    choice = int(input("Enter your choice (1/2): "))

    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle with length {length} and width {width} is: {area:.2f}")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
