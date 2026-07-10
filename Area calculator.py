import math

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"Area of triangle: {area}")

def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"Area of rectangle: {area}")

def area_square():
    side = float(input("Enter the side of the square: "))
    area = side * side
    print(f"Area of square: {area}")

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print(f"Area of circle: {area}")

def main():
    while True:
        print("\nArea Calculator")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Circle")
        print("5. Quit")
        choice = input("Select an option (1-5): ")
        if choice == '1':
            area_triangle()
        elif choice == '2':
            area_rectangle()
        elif choice == '3':
            area_square()
        elif choice == '4':
            area_circle()
        elif choice == '5':
            print("Exiting Area Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()