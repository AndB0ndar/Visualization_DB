from django.db import models


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=75)
    email = models.EmailField(max_length=100)
    inn = models.CharField(max_length=10)
    telephone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'


class StateContract(models.Model):
    id_state_contract = models.AutoField(primary_key=True)
    state = models.CharField(max_length=20)

    def __str__(self):
        return self.state

    class Meta:
        db_table = 'state_contract'


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    post = models.CharField(max_length=20)

    def __str__(self):
        return self.post

    class Meta:
        db_table = 'post'


class Employee(models.Model):
    id_employee = models.AutoField(primary_key=True)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, db_column='id_post')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telephone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


class Contract(models.Model):
    id_contract = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='id_client')
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='id_employee')
    id_state_contract = models.ForeignKey(StateContract, on_delete=models.CASCADE, db_column='id_state_contract')
    info = models.TextField()
    creation = models.DateField()
    execution = models.DateField(null=True, blank=True)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.id_contract} - {self.amount}"

    class Meta:
        db_table = 'contract'


class Warehouse(models.Model):
    id_warehouse = models.AutoField(primary_key=True)
    address = models.TextField()
    workload = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return f"{self.id_warehouse} - {self.address}"

    def is_not_empty(self):
        sql = "SELECT id_warehouse, WarehouseIsNotEmpty(%s) as is_not_empty FROM warehouse WHERE id_warehouse = %s"
        params = [self.id_warehouse, self.id_warehouse]
        result = Warehouse.objects.raw(sql, params)
        return result[0].is_not_empty if result else 0

    class Meta:
        db_table = 'warehouse'


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    id_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, db_column='id_warehouse')
    id_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True, blank=True, db_column='id_contract')
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()
    arrival = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'


class EmployeeWarehouseman(models.Model):
    id_employee = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE, db_column='id_employee')
    id_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, null=True, blank=True, db_column='id_warehouse')

    def __str__(self):
        return f"{self.id_employee} - {self.id_warehouse}"

    class Meta:
        db_table = 'employee_warehouseman'


class EmployeeDriver(models.Model):
    id_employee = models.OneToOneField(Employee, primary_key=True, on_delete=models.CASCADE, db_column='id_employee')
    license = models.CharField(max_length=12)
    end_of_action = models.DateField()

    def __str__(self):
        return self.id_employee

    class Meta:
        db_table = 'employee_driver'


class Factory(models.Model):
    id_factory = models.AutoField(primary_key=True)
    address = models.TextField()
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_factory} - {self.address}"

    class Meta:
        db_table = 'factory'


class TypeWorkshop(models.Model):
    id_type_workshop = models.AutoField(primary_key=True)
    type_workshop = models.CharField(max_length=25)

    def __str__(self):
        return self.type_workshop

    class Meta:
        db_table = 'type_workshop'


class Workshop(models.Model):
    id_workshop = models.AutoField(primary_key=True)
    id_factory = models.ForeignKey(Factory, on_delete=models.CASCADE, db_column='id_factory')
    id_type_workshop = models.ForeignKey(TypeWorkshop, on_delete=models.CASCADE, db_column='id_type_workshop')

    def __str__(self):
        return str(self.id_workshop)

    class Meta:
        db_table = 'workshop'


class Material(models.Model):
    id_material = models.AutoField(primary_key=True)
    id_workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, db_column='id_workshop')
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    arrival = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'material'


class TypeEquipment(models.Model):
    id_type_equipment = models.AutoField(primary_key=True)
    type_equipment = models.CharField(max_length=25)

    def __str__(self):
        return self.type_equipment

    class Meta:
        db_table = 'type_equipment'


class Equipment(models.Model):
    id_equipment = models.AutoField(primary_key=True)
    id_workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, db_column='id_workshop')
    id_type_equipment = models.ForeignKey(TypeEquipment, on_delete=models.CASCADE, db_column='id_type_equipment')

    def __str__(self):
        return f"{self.id_equipment} - {self.id_workshop} - {self.id_type_equipment}"

    class Meta:
        db_table = 'equipment'


class Parameter(models.Model):
    id_parameter = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parameter'


class EntryParameter(models.Model):
    id_entry_parameter = models.AutoField(primary_key=True)
    id_equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, db_column='id_equipment')
    id_parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE, db_column='id_parameter')
    date_entry = models.DateTimeField()
    value = models.TextField()

    def __str__(self):
        return f"{self.id_entry_parameter} - {self.id_equipment} - {self.id_parameter}"

    class Meta:
        db_table = 'entry_parameter'


class Transportation(models.Model):
    id_transportation = models.AutoField(primary_key=True)
    id_warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, db_column='id_warehouse')
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='id_product')
    id_factory = models.ForeignKey(Factory, on_delete=models.CASCADE, db_column='id_factory')
    id_employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='id_employee')
    dispatch = models.DateField()
    arrival = models.DateField()
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.id_transportation} - {self.id_warehouse} - {self.id_product}"

    class Meta:
        db_table = 'transportation'
        unique_together = ('id_transportation', 'id_product', 'id_warehouse', 'id_factory')


class Specialization(models.Model):
    id_specialization = models.AutoField(primary_key=True)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.specialization

    class Meta:
        db_table = 'specialization'


class EmployeeMetallurgist(models.Model):
    id_employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True, db_column='id_employee')
    id_specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_specialization')
    id_factory = models.ForeignKey(Factory, on_delete=models.SET_NULL, null=True, blank=True, db_column='id_factory')

    def __str__(self):
        return f"{self.id_employee} - {self.id_specialization} - {self.id_factory}"

    class Meta:
        db_table = 'employee_metallurgist'
