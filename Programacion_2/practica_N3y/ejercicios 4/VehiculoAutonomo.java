public class VehiculoAutonomo {
    public static String tipo = "Vehiculo Autonomo";
    private Camara camara;
    private SensorLuzLaser sensorLaser;

    public VehiculoAutonomo(String id, String resolucion, int alcance) {
        camara = new Camara(id + "-CAM", resolucion);
        sensorLaser = new SensorLuzLaser(id + "-LIDAR", alcance);
    }

    public void activarSensores() {
        camara.activar();
        sensorLaser.activar();
    }

    public void desactivarSensores() {
        camara.desactivar();
        sensorLaser.desactivar();
    }

    public void mostrarEstado() {
        System.out.println(tipo);
        System.out.println(camara);
        System.out.println(sensorLaser);
    }
}
