
class BaseCamping:
    def __init__(self, name=None, producer=None,  weight_in_kilo=None, price_in_uah=None):
        self._name = name
        self._producer = producer

        self._weight_in_kilo = weight_in_kilo
        self._price_in_uah = price_in_uah

    def __str__(self):
        name = "Name: {0}\n".format(self._name)
        producer = "Producer: {0}\n".format(self._producer)

        weight_in_kilo = "Weight in kilo: {0}\n".format(self._weight_in_kilo)
        price_in_uah = "Price in UAH: {0}\n".format(self._price_in_uah)

        return name + producer + weight_in_kilo + price_in_uah

   # def __repr__(self):
    #    return 'ThingsForBaseCamping(name=' + self.name + ', producer=' + str(self.producer) + \
     #          ', things_type=' + str(self.things_type) + ', weight_in_kilo=' + str(self.weight_in_kilo) + \
      #         ', price_in_uah=' + str(self.price_in_uah) + ')'
