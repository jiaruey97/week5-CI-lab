from shippingCalculator import ShippingCalculator
# from countryCharges import CountryCharges


class AirShippingCalculator (ShippingCalculator):


    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)


    def computeCharges(self):
        return super().baseCharge() + self.airPackagingCharge() + super().customCharge() +  self.airFreightCharges()

    def airPackagingCharge(self):
        return super().getSize()*super().getWeight()


    def airFreightCharges(self):
        return (super().getSize()*3) + (super().getWeight()*4)