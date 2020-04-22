from City import City
from Adjacent import Adjacent


class Map:
    portoUniao = City("Porto União", 203)
    pauloFrontin = City("Paulo Frontin", 172)
    canoinhas = City("Canoinhas", 141)
    irati = City("Irati", 139)
    palmeira = City("Palmeira", 59)
    campoLargo = City("Campo Largo", 27)
    curitiba = City("Curitiba", 0)
    balsaNova = City("Balsa Nova", 41)
    araucaria = City("Araucária", 23)
    saoJose = City("São José dos Pinhais", 13)
    contenda = City("Contenda", 39)
    mafra = City("Mafra", 94)
    tijucas = City("Tijucas do Sul", 56)
    lapa = City("Lapa", 74)
    soaMateus = City("São Mateus do Sul", 123)
    tresBarras = City("Três Barras", 131)

    portoUniao.addAdjacentCity(Adjacent(pauloFrontin))
    portoUniao.addAdjacentCity(Adjacent(canoinhas))
    portoUniao.addAdjacentCity(Adjacent(soaMateus))

    pauloFrontin.addAdjacentCity(Adjacent(portoUniao))
    pauloFrontin.addAdjacentCity(Adjacent(irati))

    canoinhas.addAdjacentCity(Adjacent(portoUniao))
    canoinhas.addAdjacentCity(Adjacent(tresBarras))
    canoinhas.addAdjacentCity(Adjacent(mafra))

    irati.addAdjacentCity(Adjacent(pauloFrontin))
    irati.addAdjacentCity(Adjacent(palmeira))
    irati.addAdjacentCity(Adjacent(soaMateus))

    palmeira.addAdjacentCity(Adjacent(irati))
    palmeira.addAdjacentCity(Adjacent(soaMateus))
    palmeira.addAdjacentCity(Adjacent(campoLargo))

    campoLargo.addAdjacentCity(Adjacent(palmeira))
    campoLargo.addAdjacentCity(Adjacent(balsaNova))
    campoLargo.addAdjacentCity(Adjacent(curitiba))

    curitiba.addAdjacentCity(Adjacent(campoLargo))
    curitiba.addAdjacentCity(Adjacent(balsaNova))
    curitiba.addAdjacentCity(Adjacent(araucaria))
    curitiba.addAdjacentCity(Adjacent(saoJose))

    balsaNova.addAdjacentCity(Adjacent(curitiba))
    balsaNova.addAdjacentCity(Adjacent(campoLargo))
    balsaNova.addAdjacentCity((Adjacent(contenda)))

    araucaria.addAdjacentCity(Adjacent(curitiba))
    araucaria.addAdjacentCity(Adjacent(contenda))

    saoJose.addAdjacentCity(Adjacent(curitiba))
    saoJose.addAdjacentCity(Adjacent(tijucas))

    contenda.addAdjacentCity(Adjacent(balsaNova))
    contenda.addAdjacentCity(Adjacent(araucaria))
    contenda.addAdjacentCity(Adjacent(lapa))

    mafra.addAdjacentCity(Adjacent(tijucas))
    mafra.addAdjacentCity(Adjacent(lapa))
    mafra.addAdjacentCity(Adjacent(canoinhas))

    tijucas.addAdjacentCity(Adjacent(mafra))
    tijucas.addAdjacentCity(Adjacent(saoJose))

    lapa.addAdjacentCity(Adjacent(contenda))
    lapa.addAdjacentCity(Adjacent(saoJose))
    lapa.addAdjacentCity(Adjacent(mafra))

    soaMateus.addAdjacentCity(Adjacent(palmeira))
    soaMateus.addAdjacentCity(Adjacent(irati))
    soaMateus.addAdjacentCity(Adjacent(lapa))
    soaMateus.addAdjacentCity(Adjacent(tresBarras))
    soaMateus.addAdjacentCity(Adjacent(portoUniao))

    tresBarras.addAdjacentCity(Adjacent(soaMateus))
    tresBarras.addAdjacentCity(Adjacent(canoinhas))
