# cording = utf-8
import lib.PyxlUtils as pyxl
import yaml

if __name__ == "__main__":
    xl = pyxl.PyxlTools()
    json = xl.pyxl2json(pyxl_file="D:/12. Python Src/scrapli/data/master.xlsx", key_columns="HOSTNAME")
    print(yaml.dump(json))

