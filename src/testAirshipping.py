import unittest
from airShippingCalculator import AirShippingCalculator
from landShippingCalculator import LandShippingCalculator
from seaShippingComputer import SeaShippingCalculator
from shippingCalculator import ShippingCalculator 
# from countryCharges import CountryCharges


class computeCharge(unittest.TestCase):


    def setUp(self):
        self.airJ = AirShippingCalculator("Jordan", 91234567)
        self.airJ.setFromToCountry('SG', 'USA')
        self.airJ.setSizeWeight(5, 5)
        self.airJ2 = AirShippingCalculator("James", 99234567)
        self.airJ2.setFromToCountry('SG', 'INDIA')
        self.airJ2.setSizeWeight(5, 5)

        self.landM = LandShippingCalculator("Mike", 92345678)
        self.landM.setFromToCountry('USA', 'INDIA')
        self.landM.setSizeWeight(5, 5)
        self.landM2 = LandShippingCalculator("Max", 93345678)
        self.landM2.setFromToCountry('USA', 'CHINA')
        self.landM2.setSizeWeight(5, 5)
    
        self.seaB = SeaShippingCalculator("Bane", 93456789)
        self.seaB.setFromToCountry('INDIA', 'CHINA')
        self.seaB.setSizeWeight(5, 5)
        self.seaB2 = SeaShippingCalculator("Bruno", 98456789)
        self.seaB2.setFromToCountry('INDIA', 'SG')
        self.seaB2.setSizeWeight(5, 5)

        self.cc = CountryCharges()

    def tearDown(self):
        self.airJ = None
        self.landM = None
        self.seaB = None

        self.airJ2 = None
        self.landM2 = None
        self.seaB2 = None

    def test_getBaseCharge(self):
        basecharge = self.cc.getBaseCharge('SG','USA')
        self.assertEqual(basecharge, 100)

    def test_getCustomCharges(self):
        customcharge = self.cc.getCustomCharges('USA')
        self.assertEqual(customcharge, 100)

    def test_getWeight(self):
        self.assertEqual(self.airJ.getWeight(), 5)

    def test_getSize(self):
        self.assertEqual(self.airJ.getSize(), 5)

    def test_computeCharges(self):
        self.assertEqual(self.airJ.computeCharges(), 260)
        self.assertEqual(self.airJ2.computeCharges(), 130)

        self.assertEqual(self.landM.computeCharges(), 207.5)
        self.assertEqual(self.landM2.computeCharges(), 202.5)

        self.assertEqual(self.seaB.computeCharges(), 187.5)
        self.assertEqual(self.seaB2.computeCharges(), 232.5)
