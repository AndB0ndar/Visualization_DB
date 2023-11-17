from django import forms
from .models import *


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'inn', 'telephone']


class StateContractForm(forms.ModelForm):
    class Meta:
        model = StateContract
        fields = ['state']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['id_post', 'name', 'email', 'telephone']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['id_post'].queryset = Post.objects.all()

        self.fields['id_post'].empty_label = "-"


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['id_client', 'id_employee', 'id_state_contract', 'info', 'creation', 'execution', 'amount']

    def __init__(self, *args, **kwargs):
        super(ContractForm, self).__init__(*args, **kwargs)

        self.fields['id_client'].queryset = Client.objects.all()
        self.fields['id_employee'].queryset = Employee.objects.all()
        self.fields['id_state_contract'].queryset = StateContract.objects.all()

        self.fields['id_client'].empty_label = "-"
        self.fields['id_employee'].empty_label = "-"
        self.fields['id_state_contract'].empty_label = "-"


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['address', 'workload', 'info']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id_warehouse', 'id_contract', 'title', 'quantity', 'arrival']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['id_warehouse'].queryset = Warehouse.objects.all()
        self.fields['id_contract'].queryset = Contract.objects.all()

        self.fields['id_warehouse'].empty_label = "-"
        self.fields['id_contract'].empty_label = "-"


class EmployeeWarehousemanForm(forms.ModelForm):
    class Meta:
        model = EmployeeWarehouseman
        fields = ['id_employee', 'id_warehouse']

    def __init__(self, *args, **kwargs):
        super(EmployeeWarehousemanForm, self).__init__(*args, **kwargs)

        self.fields['id_employee'].queryset = Employee.objects.all()
        self.fields['id_warehouse'].queryset = Warehouse.objects.all()

        self.fields['id_employee'].empty_label = "-"
        self.fields['id_warehouse'].empty_label = "-"


class EmployeeDriverForm(forms.ModelForm):
    class Meta:
        model = EmployeeDriver
        fields = ['id_employee', 'license', 'end_of_action']

    def __init__(self, *args, **kwargs):
        super(EmployeeDriverForm, self).__init__(*args, **kwargs)

        self.fields['id_employee'].queryset = Employee.objects.all()

        self.fields['id_employee'].empty_label = "-"


class FactoryForm(forms.ModelForm):
    class Meta:
        model = Factory
        fields = ['address', 'info']


class TypeWorkshopForm(forms.ModelForm):
    class Meta:
        model = TypeWorkshop
        fields = ['type_workshop']


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['id_factory', 'id_type_workshop']

    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)

        self.fields['id_factory'].queryset = Factory.objects.all()
        self.fields['id_type_workshop'].queryset = TypeWorkshop.objects.all()

        self.fields['id_factory'].empty_label = "-"
        self.fields['id_type_workshop'].empty_label = "-"


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['id_workshop', 'name', 'quantity', 'arrival']

    def __init__(self, *args, **kwargs):
        super(MaterialForm, self).__init__(*args, **kwargs)

        self.fields['id_workshop'].queryset = Workshop.objects.all()

        self.fields['id_workshop'].empty_label = "-"


class TypeEquipmentForm(forms.ModelForm):
    class Meta:
        model = TypeEquipment
        fields = ['type_equipment']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['id_workshop', 'id_type_equipment']

    def __init__(self, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)

        self.fields['id_workshop'].queryset = Workshop.objects.all()
        self.fields['id_type_equipment'].queryset = TypeEquipment.objects.all()

        self.fields['id_workshop'].empty_label = "-"
        self.fields['id_type_equipment'].empty_label = "-"


class ParameterForm(forms.ModelForm):
    class Meta:
        model = Parameter
        fields = ['name']


class EntryParameterForm(forms.ModelForm):
    class Meta:
        model = EntryParameter
        fields = ['id_equipment', 'id_parameter', 'date_entry', 'value']

    def __init__(self, *args, **kwargs):
        super(EntryParameterForm, self).__init__(*args, **kwargs)

        self.fields['id_equipment'].queryset = Equipment.objects.all()
        self.fields['id_parameter'].queryset = Parameter.objects.all()

        self.fields['id_equipment'].empty_label = "-"
        self.fields['id_parameter'].empty_label = "-"


class TransportationForm(forms.ModelForm):
    class Meta:
        model = Transportation
        fields = ['id_warehouse', 'id_product', 'id_factory', 'id_employee', 'dispatch', 'arrival', 'info']

    def __init__(self, *args, **kwargs):
        super(TransportationForm, self).__init__(*args, **kwargs)

        self.fields['id_warehouse'].queryset = Warehouse.objects.all()
        self.fields['id_product'].queryset = Product.objects.all()
        self.fields['id_factory'].queryset = Factory.objects.all()

        self.fields['id_warehouse'].empty_label = "Выберите оборудование"
        self.fields['id_product'].empty_label = "Выберите параметр"
        self.fields['id_factory'].empty_label = "Выберите параметр"


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ['specialization']


class EmployeeMetallurgistForm(forms.ModelForm):
    class Meta:
        model = EmployeeMetallurgist
        fields = ['id_specialization', 'id_factory']

    def __init__(self, *args, **kwargs):
        super(EmployeeMetallurgistForm, self).__init__(*args, **kwargs)

        self.fields['id_specialization'].queryset = Specialization.objects.all()
        self.fields['id_factory'].queryset = Factory.objects.all()

        self.fields['id_specialization'].empty_label = "Выберите оборудование"
        self.fields['id_factory'].empty_label = "Выберите параметр"
