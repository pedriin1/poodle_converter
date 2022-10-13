import PySimpleGUI as sg
from tkinter import Tk, font

sg.change_look_and_feel('GrayGrayGray') 
font = ("Poppins", 10)
fontmed = ("Poppins", 20)
fontbig = ("Poppins", 30)

pata = b'iVBORw0KGgoAAAANSUhEUgAAAB0AAAAYCAYAAAAGXva8AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJwSURBVHgBtVY9bNpQELYNCGqGDB4QIhG/QkgdkqVD6dasZejSrp27ZunQuRtrurI2a7PSsVky0I0gxI9ahCphMfATwAjyHfJDxnrn4KB80pOf7927e3f+7p5VxQOZTOYcj/P1em2oqmpiXm21WlW/Om4EuIV0Ol3C4z2Gbovo+dIwjOlwOGzvqyODxi3g1G9lckRU8qPjy+lzgnW6Wq0ajLzmR8eXU8uyrpC+qVOGtJmQX/vRkYEl0mg0utd1/TYQCOTxeoRxFwwGK91u978fHRlUMYnH43o0Gj2lOTY26vW6qRwAMJsOckZzRN/odDq1HafJZPI1TvsBi4L6Ct6rzWbzSnkCUqnURzeznfbUQqFgzOfzb8z+crvd3pLF1v0Eg8ebzapaC4VC186sZLPZExDpq8wYHFfg+EbDRz9VeOSdDheLxQXJKCM0YLxIMvo0Qg+yF5yx5XK5safhtPecEgxsI4DxErU6tw7JIpHINpXhcJjlgvClTSaTP0Rz5mTOOsxzxrC/KOZ2qhsSHRMH3/Rkrd/vT5HissTxz16vZzojUvgIdtZgvOK0Z9duWdjblkwikTBQKnkYoHEjCJTL5Y4R8RuuzwpomvYDOg0Q5Z+wB5KdUPNwknHHqRvkDN/0s1eEMtD1hgNcCucySDsSMRXRfYHDI8U/iMmvYrHY7WAwkJJU2nttpurKE0F7Z7PZO26da/hetbsXkOIzdk0mPCTKfWxIndr/Ooc6NX05xYbfijf+Ytw9osOuB2VCkOAX2lnRXfR0etTypasWL2R6Xhe5tGTG47GFu7UGMugY9GtpQdyCoe/uS5zTc3YzNx4A6hF4aSrL/FgAAAAASUVORK5CYII='
img_selecionarJson = b'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'
img_executar = b'iVBORw0KGgoAAAANSUhEUgAAAh8AAAAwCAYAAACxOBgbAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAbWSURBVHgB7d1PTBRnGMfxZ2ZhAUsjnvBUSbR4qtCDXtCW0Fp7qNGIt5qqSU9iUuRg0mojNP6JHKwe7KEXxYCXRqPRQ9W22fjnUHtQ7KlWUuyl4EVoIcguO2/fZ4ZZdpeVooUJi99PsmF29p2ZXRMyP573eVdHZtB4yFS58ZFWR5x3jSM1YuwDAABguiEjct8V91I66VxOdFT0P2+gU2hn47GxmpiXPmNP0igAAAAvzDnrJd2OQiHEzd/RdHSk1fXS9wgeAADg5Zldbjx9r+nwSGv+KzmVj6Yj/7TbXYcEAABgjnhiOhIHXm8Pn2fCh1Y8xMjXAgAAMNeM7PvpYOVJ3fTDh/Z46FSL3awSAACAuTfkJWNvaw+I3/Phep5OtRA8AADAfKly4ukzuuFMVj3+EAAAgHnmJVPL3JhntggAAEAUSuOf2WkXb6sAAABEwHFMo2tE6gUAACACjkiNNpzSaAoAAKJS4woAAECECB8AACBShA8AABApwgcAAIgU4QMAAESK8AEAACJVIgCKSnWVU3D/6JjIyLgRAFjoCB9AkTnxcYUsXzo9gFx7kJLOq0lZyOpWxOz7L/e33zs6KgBeTYQPoEjdf5yWgWEv87z3sScAUAwIH0CRuvbrhFx/MJGzr7LckRM7yqWyzJELd5Ny4Zfg9ZaNZdJQG5OBIU/aep75+7QKsXNDqayqduU1O75v0LPjU7aCknvOhtoSaV5XInVvxPznvX+m5cLPE3Ln92Bcw+oSaXk/7gehtu5nmeO0OnNiR4W/va97TFYtj/njQudbluQcs3ypK/s3xzPvR6/TeWU8c44vvxuTvifGfpa4/55u/zYhg38baV5bKmdvJaf9WwBYuAgfwCIy8szI970T/g36kw1xufMwLfo/KWxbG/yq7+se93/qzfur7WWZY/Sx0t70939U5oeArlvB9M3ODXqe0sw4pSFEH51XggBUaU9TbYOGkelTQdVZ00PhuOzXwmP0mt9+Wu6HjpBeQ4NUeIwGK7FH6Bjd92FdSc54AMWD8AEUqfVvxnJ6Py7enfAbTi/a6sV6W+XQyoYfJqqCRW1dN5MyOBwECA0n4b5zt1P+9jZbQQhCS6mtmqT8m30YPLLH6Tk3rSmRPXasho/Z0orKgL1+oZ4PvY4GCa3MdF4dt1UPzwYMNzO2EB2vfS463aRVEgDFg/ABFCmd7mhYPfVcb+4jQWFDjl9N+pUEDSBKb+pheNB9YTVBpzHCMX1PPD+86JTNB2tidkojOJdWPMJj1ekbyUxlZO4+S/Aeum6l/OChBoeDIKLVj0K052WhN9gCKIzwARQprU7ceThVeQirGsG254cR7YdQ2TfpYPoiEE695NMxo5PLdvOX7+r+0XGZU5WT0yeDw7lNsxqInid/LIDiQfgAitSjJ16mSpBPeyjW1079emtjaVtPMDUxODR1TFv3WMHjB4ZF6lcE0zWVs+yryB+XHXL+S1hx0b6T7M9UaEkxgOLHN5wCi5D2UOjUilZH9MauUyvNk02n2ncRVjPqV5T4N3t9aG/Iznfi/mPUTrUEzapBiNDG09CejWXy4xevSc+eYBWKrpIJx216ayrwNNTO/LdNdljpGwjOsX1daSZw6OvaXwJg8aHyARSpvRvjsisrFOjS029+SPrNoPrQPg9dOqtBI1i1Eqx+0fDRdTOVaS6tsxWOsOqgwsCitNFUw4iO06W6GjDCfpFwSe4jGz56H6eDBtfNZdJsA0T2uGxhUFHn91b4x+pS29P2fQcrW1zpaVniTyFVlosYvrAVWJSofABFKlxyGj70Zq3TLWGVQps39SZ+zv7Um74GgrCSoCtijl8ZtwHF+EtaNXhoY6mGDQ0wIW001X06TsfodXTc6evjOU2o2uAa9p+s9L+nI2hMzecfeyM4X/j+Vd9kCNH9Svf/9dRkvpMEwOLiNB0Z4W8L4BWmIUCDS3bDaiFhUJhp3GzP9X+vA6C4Me0CvOJmu3plNmFgLlbCEDqAxY9pFwAAECnCBwAAiBThAwAARIrwAQAAIkX4AAAAkXLFkX4BAACIxpDrGMIHAACIhjFy3zXGSQgAAEAEXMe95Hqp5CkBAACIQDo5ftlNdCwbckQSAgAAML/O2tzR7692Sbup3fbHkAAAAMwLM+QlUx265YePxOfL+j0jHQIAADAPPIm1a9VDtzPf85E4WHlSjNMuAAAAc8iz+SJxYEmmx9TJH9B4eKTVdeSQ3awSAACAl2anWrTikRU8lFNoaOOxpzWuV6oBZJcAAAC8IGMkYVKp3eFUSzZnpgM1hMS8ki12OmarcUy9HU41BAAAFNJvA0e/ESchqeQpXU37vIH/Ah82ougCmu1RAAAAAElFTkSuQmCC'

BAR_MAX = 1000


graph = sg.Graph((600,600), (0,0), (600,600), key='-G-')

layout = [
    [sg.Text("Gerador .poodle", size=20, font=fontbig)],
    [sg.Text("Escolha o arquivo Json: ")],
    [sg.Input("ex: conta.json", size=65), sg.FileBrowse(
        "Selecionar Json",  file_types=(("Arquivos Json",  "*.json"),), key="fileJson", button_color=('#FFFFFF','#0F9D58')),],
    [sg.Text("Insira o caminho para salvar o arquivo: ")],
   
    [sg.Input(str(r"C:\Users\giovannimori"), size=63, key="savePath"), sg.FileBrowse(
        "Selecionar Destino", file_types=(("Arquivos Json", "*.json"),), key="fileJson", button_color=('#FFFFFF','#0F9D58'))],
    [sg.Text("Quantide de MB:      ")],
    [
      [sg.CB('2', key='-2-', change_submits=True),
           sg.CB('3', key='-3-', change_submits=True),
           sg.CB('4', key='-4-', change_submits=True)]],
    [sg.Button("", key="Enviar", image_data=img_executar, border_width=1, button_color='#4285F4')], [sg.T("")],
    [graph]
   
]



background_layout = [[sg.Image(data=img_selecionarJson)]]


# window_background = sg.Window('Background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[[''], ['Exit',]])
# Building Window


top_window = sg.Window('Everything bagel', layout, finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color(), no_titlebar=True)


window = sg.Window('Poodle Generator ', background_layout,
                   icon='poodle.ico', size=(1280, 832),font=font)
top_window.bring_to_front()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Enviar":
        graph.draw_image(image_source=pata, location=(20,20))
        print(values["valueMB"])
        print(values["fileJson"])

window.close()
