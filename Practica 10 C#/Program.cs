//Brenda Lizeth Palasio Gutiérrez
//Suma Recursiva e Iterativa

using System;

class Program
{
    static int SumaIterativa(int n)
    {
        int suma = 0;
        while (n > 9)
        {
            suma += n % 10;
            n /= 10;
        }
        suma += n;
        return suma;
    }

    static int SumaRecursiva(int n)
    {
        if (n <= 9)
            return n;
        else
            return SumaRecursiva(n / 10) + n % 10;
    }

    static void Main()
    {
        int opcion, numero;

        Console.Write("Ingrese un numero para la suma: ");
        if (int.TryParse(Console.ReadLine(), out numero))
        {
            Console.Write("Elija una opcion (1 para suma recursiva, 2 para suma iterativa): ");
            if (int.TryParse(Console.ReadLine(), out opcion))
            {
                if (opcion == 1)
                {
                    Console.WriteLine("Suma recursiva: " + SumaRecursiva(numero));
                }
                else if (opcion == 2)
                {
                    Console.WriteLine("Suma iterativa: " + SumaIterativa(numero));
                }
                else
                {
                    Console.WriteLine("Opcion no valida.");
                }
            }
            else
            {
                Console.WriteLine("Opcion no valida.");
            }
        }
        else
        {
            Console.WriteLine("Numero no valido.");
        }
    }
}