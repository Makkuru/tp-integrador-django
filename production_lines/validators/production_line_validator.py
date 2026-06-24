"""Validadores de entrada para lineas de produccion."""

from production_lines.models.production_line import ProductionLine


class ProductionLineValidator:
    """Verifica integridad de datos antes de procesarlos."""

    @staticmethod
    def validate_status(status):
        if status not in ProductionLine.STATUSES:
            valid = ', '.join(ProductionLine.STATUSES)
            raise ValueError(f'Estado invalido. Estados permitidos: {valid}.')
