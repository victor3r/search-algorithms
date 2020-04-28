from City import City
from Adjacent import Adjacent


class Map:
    def __init__(self):
        self.portoUniao = City("Porto União", 203)
        self.pauloFrontin = City("Paulo Frontin", 172)
        self.canoinhas = City("Canoinhas", 141)
        self.irati = City("Irati", 139)
        self.palmeira = City("Palmeira", 59)
        self.campoLargo = City("Campo Largo", 27)
        self.curitiba = City("Curitiba", 0)
        self.balsaNova = City("Balsa Nova", 41)
        self.araucaria = City("Araucária", 23)
        self.saoJose = City("São José dos Pinhais", 13)
        self.contenda = City("Contenda", 39)
        self.mafra = City("Mafra", 94)
        self.tijucas = City("Tijucas do Sul", 56)
        self.lapa = City("Lapa", 74)
        self.saoMateus = City("São Mateus do Sul", 123)
        self.tresBarras = City("Três Barras", 131)

        self.portoUniao.addAdjacentCity(Adjacent(self.pauloFrontin, 46))
        self.portoUniao.addAdjacentCity(Adjacent(self.canoinhas, 78))
        self.portoUniao.addAdjacentCity(Adjacent(self.saoMateus, 87))

        self.pauloFrontin.addAdjacentCity(Adjacent(self.portoUniao, 46))
        self.pauloFrontin.addAdjacentCity(Adjacent(self.irati, 75))

        self.canoinhas.addAdjacentCity(Adjacent(self.portoUniao, 78))
        self.canoinhas.addAdjacentCity(Adjacent(self.tresBarras, 12))
        self.canoinhas.addAdjacentCity(Adjacent(self.mafra, 66))

        self.irati.addAdjacentCity(Adjacent(self.pauloFrontin, 75))
        self.irati.addAdjacentCity(Adjacent(self.palmeira, 75))
        self.irati.addAdjacentCity(Adjacent(self.saoMateus, 57))

        self.palmeira.addAdjacentCity(Adjacent(self.irati, 75))
        self.palmeira.addAdjacentCity(Adjacent(self.saoMateus, 77))
        self.palmeira.addAdjacentCity(Adjacent(self.campoLargo, 55))

        self.campoLargo.addAdjacentCity(Adjacent(self.palmeira, 55))
        self.campoLargo.addAdjacentCity(Adjacent(self.balsaNova, 22))
        self.campoLargo.addAdjacentCity(Adjacent(self.curitiba, 29))

        self.curitiba.addAdjacentCity(Adjacent(self.campoLargo, 29))
        self.curitiba.addAdjacentCity(Adjacent(self.balsaNova, 51))
        self.curitiba.addAdjacentCity(Adjacent(self.araucaria, 37))
        self.curitiba.addAdjacentCity(Adjacent(self.saoJose, 15))

        self.balsaNova.addAdjacentCity(Adjacent(self.curitiba, 51))
        self.balsaNova.addAdjacentCity(Adjacent(self.campoLargo, 22))
        self.balsaNova.addAdjacentCity((Adjacent(self.contenda, 19)))

        self.araucaria.addAdjacentCity(Adjacent(self.curitiba, 37))
        self.araucaria.addAdjacentCity(Adjacent(self.contenda, 18))

        self.saoJose.addAdjacentCity(Adjacent(self.curitiba, 15))
        self.saoJose.addAdjacentCity(Adjacent(self.tijucas, 49))

        self.contenda.addAdjacentCity(Adjacent(self.balsaNova, 19))
        self.contenda.addAdjacentCity(Adjacent(self.araucaria, 18))
        self.contenda.addAdjacentCity(Adjacent(self.lapa, 26))

        self.mafra.addAdjacentCity(Adjacent(self.tijucas, 99))
        self.mafra.addAdjacentCity(Adjacent(self.lapa, 57))
        self.mafra.addAdjacentCity(Adjacent(self.canoinhas, 66))

        self.tijucas.addAdjacentCity(Adjacent(self.mafra, 99))
        self.tijucas.addAdjacentCity(Adjacent(self.saoJose, 49))

        self.lapa.addAdjacentCity(Adjacent(self.contenda, 26))
        self.lapa.addAdjacentCity(Adjacent(self.saoMateus, 60))
        self.lapa.addAdjacentCity(Adjacent(self.mafra, 57))

        self.saoMateus.addAdjacentCity(Adjacent(self.palmeira, 77))
        self.saoMateus.addAdjacentCity(Adjacent(self.irati, 57))
        self.saoMateus.addAdjacentCity(Adjacent(self.lapa, 60))
        self.saoMateus.addAdjacentCity(Adjacent(self.tresBarras, 43))
        self.saoMateus.addAdjacentCity(Adjacent(self.portoUniao, 87))

        self.tresBarras.addAdjacentCity(Adjacent(self.saoMateus, 43))
        self.tresBarras.addAdjacentCity(Adjacent(self.canoinhas, 12))
