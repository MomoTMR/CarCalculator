import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(
        calculator.Car("Toyota Prius", 120000, 7,1200,2500)
    )
    calc.add_car(
        calculator.ElectricCar("Tesla Model 3",200000,5500,150)
    )
    calc.print_cars()