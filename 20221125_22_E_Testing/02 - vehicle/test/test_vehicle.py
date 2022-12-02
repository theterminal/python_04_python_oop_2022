from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_1_init_correct_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_2_init_correct(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_3_drive_without_enough_fuel_rise_exeption(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(12)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_4_drive_w_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(8, self.vehicle.fuel)

    def test_5_refuel_w_excess_fuel_rise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_6_refuel_w_ok_amount(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(10)
        self.assertEqual(10, self.vehicle.fuel)

    def test_6_str_message(self):
        self.assertEqual('The vehicle has 175.5 horse power with 20.5 fuel left and 1.25 fuel consumption', str(self.vehicle))


if __name__ == '__main__':
    main()
