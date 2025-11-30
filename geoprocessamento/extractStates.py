#Codigo que usa a biblioteca geopandas para extrair de um shapefile com todos os municipios do Brasil apenas um estado

import geopandas as gpd
from pathlib import Path

ESTADO = "MG"

def main(args=None):
    base = Path(__file__).resolve().parent
    caminho_shape = base / "shapefile" / "municipios.shp"

    gdf = gpd.read_file(caminho_shape)
    print(f"Lido: {caminho_shape} | feições: {len(gdf)} | CRS: {gdf.crs}")
    municipios_filtrados = gdf[gdf["SIGLA"] == ESTADO]
    print(f"lido em {ESTADO}| feições: {len(municipios_filtrados)} | CRS: {municipios_filtrados.crs}")
    municipios_filtrados.to_file(f"municipios_{ESTADO}.shp")

if __name__ == "__main__":
    main()