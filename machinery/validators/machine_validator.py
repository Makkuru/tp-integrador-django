"""Validadores de entrada para maquinaria."""

from machinery.models.machine import Machine


class MachineValidator:
    """Verifica integridad de datos antes de procesarlos."""

    @staticmethod
    def validate_status(status):
        if status not in Machine.STATUSES:
            valid = ', '.join(Machine.STATUSES)
            raise ValueError(f'Estado invalido. Estados permitidos: {valid}.')
