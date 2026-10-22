public class Aplicacion2 {
    public static void main(String[] args) {
        CriaturaMarina[] elementos = {
            new Calamar("Octavio"),
            new Delfin("Flipper"),
            new Mamifero("Manny"),
            new CriaturaMarina("Marina"),
            new Ballena("Willy")
        };

        for (CriaturaMarina elemento : elementos) {
            elemento.metodo2();
            System.out.println(elemento);
            elemento.metodo1();
            System.out.println();
        }

        // nadar() se invoca explícitamente porque no está definido en CriaturaMarina.
        Ballena ballena = new Ballena("Willy");
        ballena.nadar();
    }
}
