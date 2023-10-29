//Brenda Lizeth Palasio Gutiérrez
//Suma Recursiva e Iterativa

#include <iostream>

using namespace std;

int SumaIterativa(int n) {
    int suma = 0;
    while (n > 9) {
        suma += n % 10;
        n /= 10;
    }
    suma += n;
    return suma;
}

int SumaRecursiva(int n) {
    if (n <= 9)
        return n;
    else
        return SumaRecursiva(n / 10) + n % 10;
}

int main() {
    int opcion, numero;

    cout << "Ingrese un numero para la suma: ";
    cin >> numero;

    cout << "Elija una opcion (1 para suma recursiva, 2 para suma iterativa): ";
    cin >> opcion;

    if (opcion == 1) {
        cout << "Suma recursiva: " << SumaRecursiva(numero) << endl;
    }
    else if (opcion == 2) {
        cout << "Suma iterativa: " << SumaIterativa(numero) << endl;
    }
    else {
        cout << "Opcion no valida." << endl;
    }

    return 0;
}
