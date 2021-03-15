from crud import *
from database import *


if __name__ == "__main__":
    try:
        criar_db()
    except:
        print("Banco de Dados já foi criado!")

    crud.mainloop()
