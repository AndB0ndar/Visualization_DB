from django.db import connections
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import *
from .models import *


def main(request):
    return render(request, 'wdb/main.html', {'urls': ModelFactory.titles.items()})


class ModelFactory:
    titles = {
        'clients': "Client List"
        , 'state_contracts': "State Contracts List"
        , 'posts': "Posts List"
        , 'employees': "Employees List"
        , 'contracts': "Contracts List TRIGGER(check date)"
        , 'warehouses': "Warehouses List FUNCTION"
        , 'products': "Products List TRIGGER(time) & PROCEDURE(amount)"
        , 'employee_warehouseman': "Employee Warehouseman List"
        , 'employee_drivers': "Employee Drivers List"
        , 'factories': "Factories List"
        , 'type_workshops': "Type Workshops List"
        , 'workshops': "Workshops List"
        , 'materials': "Materials List"
        , 'type_equipments': "Type_equipments List"
        , 'equipments': "Equipments List"
        , 'parameters': "Parameters List"
        , 'entry_parameters': "Entry_parameters List"
        , 'transportations': "Transportations List"
        , 'specializations': "Specializations List"
        , 'employee_metallurgists': "Employee Metallurgists List"
    }
    htmls = {
        'clients': "wdb/client_list.html"
        , 'state_contracts': "wdb/state_contract_list.html"
        , 'posts': "wdb/post_list.html"
        , 'employees': "wdb/employee_list.html"
        , 'contracts': "wdb/contract_list.html"
        , 'warehouses': "wdb/warehouse_list.html"
        , 'products': "wdb/product_list.html"
        , 'employee_warehouseman': "wdb/employee_warehouseman_list.html"
        , 'employee_drivers': "" "wdb/employee_driver_list.html"
        , 'factories': "wdb/factory_list.html"
        , 'type_workshops': "wdb/type_workshop_list.html"
        , 'workshops': "wdb/workshop_list.html"
        , 'materials': "wdb/material_list.html"
        , 'type_equipments': "wdb/type_equipment_list.html"
        , 'equipments': "wdb/equipment_list.html"
        , 'parameters': "wdb/parameter_list.html"
        , 'entry_parameters': "wdb/entry_parameter_list.html"
        , 'transportations': "wdb/transportation_list.html"
        , 'specializations': "wdb/specialization_list.html"
        , 'employee_metallurgists': "wdb/employee_metallurgist_list.html"
    }

    def create_title(self, model_type):
        return self.titles[model_type]

    def create_html(self, model_type):
        return self.htmls[model_type]

    def create_model_class(self, model_type: str):
        if model_type == 'clients':
            return Client
        elif model_type == 'employees':
            return Employee
        elif model_type == 'contracts':
            return Contract
        elif model_type == 'state_contracts':
            return StateContract
        elif model_type == 'posts':
            return Post
        elif model_type == 'employees':
            return Employee
        elif model_type == 'contracts':
            return Contract
        elif model_type == 'warehouses':
            return Warehouse
        elif model_type == 'products':
            return Product
        elif model_type == 'employee_warehouseman':
            return EmployeeWarehouseman
        elif model_type == 'employee_drivers':
            return EmployeeDriver
        elif model_type == 'factories':
            return Factory
        elif model_type == 'type_workshops':
            return TypeWorkshop
        elif model_type == 'workshops':
            return Workshop
        elif model_type == 'materials':
            return Material
        elif model_type == 'type_equipments':
            return TypeEquipment
        elif model_type == 'equipments':
            return Equipment
        elif model_type == 'parameters':
            return Parameter
        elif model_type == 'entry_parameters':
            return EntryParameter
        elif model_type == 'transportations':
            return Transportation
        elif model_type == 'specializations':
            return Specialization
        elif model_type == 'employee_metallurgists':
            return EmployeeMetallurgist

    def create_filter_objects(self, model_type: str, filter=None):
        if model_type == 'clients':
            return Client.objects.filter(name__icontains=filter)
        elif model_type == 'employees':
            return Employee.objects.filter(name__icontains=filter)
        elif model_type == 'contracts':
            return Contract.objects.filter(amount__icontains=filter)
        elif model_type == 'state_contracts':
            return StateContract.objects.filter(state__icontains=filter)
        elif model_type == 'posts':
            return Post.objects.filter(post__icontains=filter)
        elif model_type == 'employees':
            return Employee.objects.filter(name__icontains=filter)
        elif model_type == 'contracts':
            return Contract.objects.filter(name__icontains=filter)
        elif model_type == 'warehouses':
            return Warehouse.objects.filter(address__icontains=filter)
        elif model_type == 'products':
            return Product.objects.filter(title__icontains=filter)
        elif model_type == 'factories':
            return Factory.objects.filter(address__icontains=filter)
        elif model_type == 'type_workshops':
            return TypeWorkshop.objects.filter(type_workshop__icontains=filter)
        elif model_type == 'materials':
            return Material.objects.filter(name__icontains=filter)
        elif model_type == 'type_equipments':
            return TypeEquipment.objects.filter(type_equipment__icontains=filter)
        elif model_type == 'parameters':
            return Parameter.objects.filter(name__icontains=filter)
        elif model_type == 'entry_parameters':
            return EntryParameter.objects.filter(date_entry__icontains=filter)
        elif model_type == 'transportations':
            return Transportation.objects.filter(arrival__icontains=filter)
        elif model_type == 'specializations':
            return Specialization.objects.filter(specialization__icontains=filter)

    def create_form(self, model_type: str, data=None, instance=None):
        if model_type == 'clients':
            return ClientForm(data=data, instance=instance)
        elif model_type == 'employees':
            return EmployeeForm(data=data, instance=instance)
        elif model_type == 'contracts':
            return ContractForm(data=data, instance=instance)
        elif model_type == 'state_contracts':
            return StateContractForm(data=data, instance=instance)
        elif model_type == 'posts':
            return PostForm(data=data, instance=instance)
        elif model_type == 'employees':
            return EmployeeForm(data=data, instance=instance)
        elif model_type == 'contracts':
            return ContractForm(data=data, instance=instance)
        elif model_type == 'warehouses':
            return WarehouseForm(data=data, instance=instance)
        elif model_type == 'products':
            return ProductForm(data=data, instance=instance)
        elif model_type == 'employee_warehouseman':
            return EmployeeWarehousemanForm(data=data, instance=instance)
        elif model_type == 'employee_drivers':
            return EmployeeDriverForm(data=data, instance=instance)
        elif model_type == 'factories':
            return FactoryForm(data=data, instance=instance)
        elif model_type == 'type_workshops':
            return TypeWorkshopForm(data=data, instance=instance)
        elif model_type == 'workshops':
            return WorkshopForm(data=data, instance=instance)
        elif model_type == 'materials':
            return MaterialForm(data=data, instance=instance)
        elif model_type == 'type_equipments':
            return TypeEquipmentForm(data=data, instance=instance)
        elif model_type == 'equipments':
            return EquipmentForm(data=data, instance=instance)
        elif model_type == 'parameters':
            return ParameterForm(data=data, instance=instance)
        elif model_type == 'entry_parameters':
            return EntryParameterForm(data=data, instance=instance)
        elif model_type == 'transportations':
            return TransportationForm(data=data, instance=instance)
        elif model_type == 'specializations':
            return SpecializationForm(data=data, instance=instance)
        elif model_type == 'employee_metallurgists':
            return EmployeeMetallurgistForm(data=data, instance=instance)


def count_product(warehouse_id):
    return Warehouse.objects.filter(id_warehouse=warehouse_id).annotate(product_count=models.Count('product')).values('product_count').first()['product_count']


def perform_amount(id_contract):
    with connections['default'].cursor() as cursor:
        cursor.callproc('perfon_amount', [int(id_contract)])


def get_employee_by_post(post):
    with connections['default'].cursor() as cursor:
        cursor.callproc('SELECT_EMPLOYY_BY_POST', [post])
        result = cursor.fetchall()
        return [item[0] for item in result]


def tables(request, model_type):
    print("TABLE==========", model_type)
    objects = ModelFactory().create_model_class(model_type).objects.all()
    search_query = request.GET.get('q')

    if search_query:
        objects =  ModelFactory().create_filter_objects(model_type, filter=search_query)

    context = {
        'title': ModelFactory().create_title(model_type)
        , model_type: objects
        , 'form': ModelFactory().create_form(model_type)
        , 'search_query': search_query
    }

    if model_type == "warehouses":
        context[model_type] = [(warehouse, count_product(warehouse.id_warehouse), warehouse.is_not_empty()) for warehouse in objects]

    if request.method == 'POST':
        form = ModelFactory().create_form(model_type, data=request.POST)
        if form.is_valid():
            instance = form.save()
            if model_type == "products":
                perform_amount(instance.id_contract.id_contract)
            return redirect('list', model_type)
        else:
            print(form.errors)
    return render(request, ModelFactory().create_html(model_type), context)


def delete(request, model_type, model_id):
    object = get_object_or_404(ModelFactory().create_model_class(model_type), pk=model_id)
    object.delete()
    return redirect('list', model_type)


def update(request, model_type, model_id):
    print("UPDATE=========", model_type)
    model_class = ModelFactory().create_model_class(model_type)
    if model_id:
        instance = get_object_or_404(model_class, pk=model_id)
    else:
        instance = None
    if request.method == 'POST':
        form = ModelFactory().create_form(model_type, data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('list', model_type)
        else:
            print(form.errors)
    else:
        form = ModelFactory().create_form(model_type, instance=instance)
    context = {
        'title': ModelFactory().create_title(model_type),
        'form': form,
        'model_type': model_type,
        'model_id': model_id
    }
    return render(request, "wdb/update.html", context)


def employee_by_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            result = get_employee_by_post(form.cleaned_data['post'])
            return render(request, 'wdb/employee_by_post.html', {'result': result, 'form': PostForm()})
    else:
        form = PostForm()

    return render(request, 'wdb/employee_by_post.html', {'form': form})
