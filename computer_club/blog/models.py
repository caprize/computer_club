# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Breakage(models.Model):
    type = models.IntegerField()
    computer = models.ForeignKey('Computer', models.DO_NOTHING)
    date_finish = models.DateField()
    engineer = models.ForeignKey('Engineer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'breakage'
    def __str__(self):
        return str(self.type)




class ComputerClub(models.Model):
    addres = models.CharField(max_length=255)
    isworking = models.IntegerField(db_column='isWorking')  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'computer_club'
    def __str__(self):
        return self.addres

class Computer(models.Model):
    status = models.IntegerField()
    computer_club = models.ForeignKey(ComputerClub, models.DO_NOTHING)
    isworking = models.IntegerField(db_column='isWorking')  # Field name made lowercase.
    price = models.IntegerField(default=0)
    class Meta:
        managed = False
        db_table = 'computer'
    def __str__(self):
        return "Id " + str(self.id) +" Price is: "+ str(self.price)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Engineer(models.Model):
    name = models.CharField(max_length=255)
    work_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'engineer'


class OrderTable(models.Model):
    computer = models.ForeignKey(Computer, models.DO_NOTHING)
    computer_club = models.ForeignKey(ComputerClub, models.DO_NOTHING)
    date_end = models.DateTimeField()
    date_start = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'order_table'
    def __str__(self):
        return "Order for " + str(self.date_start)[11:18] + ". In : " + self.computer_club.addres + ". Computer id is : " + str(self.computer.id) 


class Payment(models.Model):
    amount = models.IntegerField()
    isaccepted = models.IntegerField(db_column='isAccepted')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class User(models.Model):
    name = models.CharField(max_length=255)
    isusing = models.IntegerField(db_column='isUsing')  # Field name made lowercase.
    order = models.ForeignKey(OrderTable, models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey(Payment, models.DO_NOTHING, blank=True, null=True)
    passw = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.DateField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'user'
