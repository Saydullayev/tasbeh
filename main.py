import flet as ft

k = 0
def main(page: ft.Page):
    brr = [0,0,0]
    arr = ['Subhan Alloh','Alhamdulillah','Allohu Akbar']


    page.window_width = '300'
    page.window_height = '600'
    page.window_always_on_top = True
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme_mode = 'dark'
    page.title = 'Counter'


    norm = ft.Text(
        value = 'Subhan Alloh',
        size = 25,
        font_family="Bahnschrift"
    )

    counter = ft.Text(
        value=33,
        size=80,
        font_family="Bahnschrift"
    )

    subh = ft.Text(
        value = arr[0] +' '+ str(brr[0]),
        size = 10
    )

    alha = ft.Text(
        value = arr[1] +' '+ str(brr[1]),
        size = 10
    )

    akba = ft.Text(
        value = arr[2] +" "+ str(brr[2]),
        size = 10
    )


    def r_val(e):
        global k
        if counter.value == '':
            counter.value = 34
            norm.value = arr[0]
        if arr.index(norm.value) == 2 and counter.value == 1:
            but.icon = 'add'
            but.bgcolor = 'blue'
        else:
            but.icon = 'remove'
            but.bgcolor = 'red'
        counter.value -= 1

        if counter.value == 0:
            brr[arr.index(norm.value)] += 1
            if k == 0:
                subh.value = arr[0] +' '+ str(brr[arr.index(norm.value)])
            elif k == 1:
                alha.value = arr[1] +' '+ str(brr[arr.index(norm.value)])
            else:
                akba.value = arr[2] +' '+ str(brr[arr.index(norm.value)])
            k += 1
            k %= 3
            page.update()
            print(brr[arr.index(norm.value)])
            counter.value = 33

            if arr.index(norm.value)+1 == 3:
                norm.value = 'The end, try again?'
                norm.size = 30
                counter.value = ''
            else:
                norm.value = arr[arr.index(norm.value)+1]
        
        page.update()


    but = ft.FloatingActionButton(icon='remove', on_click=r_val, bgcolor='red',tooltip='')
    

    page.add(norm,counter,but,subh,alha,akba)

    page.update()

ft.app(target=main, view='flet_app')