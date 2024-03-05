class persona{
    tomarMedicamentos(){
        medicamento.MedicamentoTomado();
        Alarma.calcularSiguienteAlarma();
    }

}
class medicamento{
    cantidad;
    restockMedicamento(cantidades){
        this.cantidad=cantidades;//ir a comprar medicamentos
    }
    MedicamentoTomado(){
        medicamento.cantidad-=1;
    }

    

}
class Alarma{
    //todo el sistema supone que estos datos son:
    cantidad
    CantidadAlarmas=8;//horas
    horaAlarma;//tiempo
    empezarAlarmas(){
        this.horaAlarma=horaActual;//hora actual es la hora precisa del momento
        
    }
    calcularSiguienteAlarma(){
        if (this.CantidadAlarmas =!0){
        this.CantidadAlarmas-=1;
        this.HoraAlarma+=8;
        }
        this.NotificacionAlarma();
        
    }
    NotificacionAlarma(){
        if (this.HoraAlarma=horaActual){
        persona.tomarMedicamentos();
        this.calcularSiguienteAlarma();
        }
        
    }


}

//empezar alarmas
//tomar medicamento