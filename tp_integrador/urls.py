"""
URL configuration for tp_integrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from machinery.controllers.machine_controller import MachineController
from operators.controllers.operator_controller import OperatorController
from production_lines.controllers.production_line_controller import ProductionLineController
from production_orders.controllers.production_order_controller import ProductionOrderController
from raw_materials.controllers.raw_material_controller import RawMaterialController

production_order_controller = ProductionOrderController()
raw_material_controller = RawMaterialController()
machine_controller = MachineController()
operator_controller = OperatorController()
production_line_controller = ProductionLineController()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('production-orders/', production_order_controller.get_all),
    path('production-orders/create/', production_order_controller.create),
    path('production-orders/<int:order_id>/', production_order_controller.get_by_id),
    path('production-orders/<int:order_id>/status/', production_order_controller.change_status),
    path('raw-materials/', raw_material_controller.get_all),
    path('raw-materials/create/', raw_material_controller.create),
    path('raw-materials/<int:material_id>/', raw_material_controller.get_by_id),
    path('raw-materials/<int:material_id>/stock/', raw_material_controller.update_stock),
    path('machinery/', machine_controller.get_all),
    path('machinery/<int:machine_id>/', machine_controller.get_by_id),
    path('machinery/<int:machine_id>/status/', machine_controller.change_status),
    path('operators/', operator_controller.get_all),
    path('operators/create/', operator_controller.create),
    path('operators/<int:operator_id>/', operator_controller.get_by_id),
    path('operators/<int:operator_id>/activate/', operator_controller.activate),
    path('operators/<int:operator_id>/deactivate/', operator_controller.deactivate),
    path('production-lines/', production_line_controller.get_all),
    path('production-lines/<int:line_id>/', production_line_controller.get_by_id),
    path('production-lines/<int:line_id>/activate/', production_line_controller.activate),
    path('production-lines/<int:line_id>/deactivate/', production_line_controller.deactivate),
]
