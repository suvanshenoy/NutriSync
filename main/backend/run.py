from app import create_app
from colorama import Fore,Style

app = create_app()

HOST = 'localhost'
DEBUG = True
default_port_mesg = "[default : '3000']"
PORT = int(input(f"{Fore.CYAN}enter the port number{Fore.GREEN} {default_port_mesg}\n{Fore.CYAN}=>  {Style.RESET_ALL}"))



if __name__ == '__main__':
    app.run(port=PORT,host=HOST,debug=DEBUG)
