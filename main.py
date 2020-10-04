from controller.login_controller import Login_controller
from helpers.menu import Menu
import pprint


def iniciar_app():


    try:
        print('''
        =======================
            Sistema Market
        =======================
        ''')
        menu_principal = ["Login", "Salir"]
        respuesta = Menu(menu_principal).show()        
        
        if respuesta == 1:
            
            login = Login_controller()
            login.logeo()
            if login.salir:
                iniciar_app()

        elif respuesta == 2:
            
            pass

        elif respuesta == 3:
            
            pass

        print("\nGracias por utilizar nuestro sistema bibliotecario\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()