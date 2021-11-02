from shippingCalculator import ShippingCalculator
# from countryCharges import CountryCharges


class LandShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        return super().baseCharge() + self.landPackagingCharge() + super().customCharge() + self.landFreightCharges()

    def landPackagingCharge(self):
        return (super().getSize()*super().getWeight())*0.9

    def landFreightCharges(self):
        return (super().getSize()*0.25) + (super().getWeight()*0.75) + 10
