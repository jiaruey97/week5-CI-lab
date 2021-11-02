from shippingCalculator import ShippingCalculator
# from countryCharges import CountryCharges


class SeaShippingCalculator (ShippingCalculator):


    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self,custNm, custContact)


    def computeCharges(self):
        return super().baseCharge() + self.seaPackagingCharge() + super().customCharge() + self.seaFreightCharges()


    def seaPackagingCharge(self):
        return super().getSize()*super().getWeight()


    def seaFreightCharges(self):
        return (super().getSize()*0.75) + (super().getWeight()*0.75) + 100