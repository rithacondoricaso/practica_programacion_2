public class CriaturaMarina {
    protected String nombre;

    public CriaturaMarina() {
        this("Marina");
    }

    public CriaturaMarina(String nombre) {
        this.nombre = nombre;
    }

    public void metodo1() {
        System.out.println("criatura 1");
    }

    public void metodo2() {
        System.out.println("criatura 2");
    }

    @Override
    public String toString() {
        return "habita en el oceano" + (nombre == null ? "" : ": " + nombre);
    }
}

class Mamifero extends CriaturaMarina {
    public Mamifero() { super(); }
    public Mamifero(String nombre) { super(nombre); }

    @Override
    public void metodo1() {
        System.out.println("sangre caliente");
    }

    @Override
    public String toString() {
        return "mamifero: " + nombre;
    }
}

class Delfin extends Mamifero {
    public Delfin() { super("Delfin"); }
    public Delfin(String nombre) { super(nombre); }

    @Override
    public void metodo1() {
        System.out.println("sopla burbujas");
        super.metodo1();
    }

    @Override
    public String toString() {
        return "delfin: " + nombre;
    }
}

class Calamar extends CriaturaMarina {
    public Calamar() { super("Calamar"); }
    public Calamar(String nombre) { super(nombre); }

    @Override
    public void metodo2() {
        System.out.println("tentaculos");
    }

    @Override
    public String toString() {
        return "calamar: " + nombre + " tentaculos";
    }
}

class Ballena extends Mamifero {
    public Ballena() { super("Ballena"); }
    public Ballena(String nombre) { super(nombre); }

    @Override
    public void metodo1() {
        System.out.println("canta canciones");
    }

    @Override
    public String toString() {
        return "ballena: " + nombre;
    }

    public void nadar() {
        System.out.println("nada profundamente");
    }
}
