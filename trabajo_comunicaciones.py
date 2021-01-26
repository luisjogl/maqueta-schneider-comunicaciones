from opcua import Client
from opcua import ua
import time
import variables
from menu import menu

def main():
    # Establece conexion y define variables empleadas
    client = Client("opc.tcp://10.0.0.51:4840")              # construye un objeto cliente OPC UA para un servidor
    try:
        print("Conectando")
        client.connect()                                         # conecta el objeto cliente
        root = client.get_root_node()                             # navegacion a traves del arbol de objetos
        objects = root.get_child(['0:Objects'])
        m241 = objects.get_child(['2:M241-M251 data'])
        variables.get_POU_variables(m241)
        MainWindow.show()

    finally:
        print("Desconectando")
        client.disconnect()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    main()
    
    sys.exit(app.exec_())

