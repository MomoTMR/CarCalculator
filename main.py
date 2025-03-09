import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Toyota Prius", 120000, 7,1200,2500)
    )
    calc.add_car(
        calculator.Car("Range Rover", 200000, 5500, 150,3000)
    )
    calc.print_cars()