# Generated by Django 3.2.12 on 2022-03-31 12:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointmentId', models.AutoField(primary_key=True, serialize=False)),
                ('caseNumber', models.IntegerField(blank=True, null=True, verbose_name='Case Number')),
                ('patientName', models.CharField(max_length=24, verbose_name='Patient Name')),
                ('patientEmail', models.EmailField(max_length=254, unique=True, verbose_name='Email Id')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.IntegerField(unique=True, validators=[home.models.validate_phoneNumber], verbose_name='Phone Number')),
                ('patientRelativeNumber', models.IntegerField(validators=[home.models.validate_phoneNumber], verbose_name="Relative's Phone number")),
                ('patientRelativeName', models.CharField(max_length=24, verbose_name="Relative's name")),
                ('reason', models.CharField(max_length=250, verbose_name='Reason')),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('bedId', models.AutoField(primary_key=True, serialize=False)),
                ('bedNumber', models.CharField(max_length=5, verbose_name='Bed Number')),
                ('occupied', models.BooleanField(default=False, verbose_name='Occupied')),
            ],
        ),
        migrations.CreateModel(
            name='block',
            fields=[
                ('blockId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(default=None, max_length=100, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityId', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=24, unique=True, verbose_name='City Name')),
            ],
        ),
        migrations.CreateModel(
            name='configuration',
            fields=[
                ('configurationId', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=10)),
                ('fieldname', models.CharField(default=None, max_length=10, unique=True)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('contactId', models.AutoField(primary_key=True, serialize=False)),
                ('contactName', models.CharField(max_length=24, verbose_name='Name')),
                ('contactEmail', models.EmailField(max_length=24, verbose_name='Email')),
                ('contactNo', models.IntegerField(null=True, validators=[home.models.validate_phoneNumber], verbose_name='Number')),
                ('contactMsg', models.CharField(max_length=300, verbose_name='Massage')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorId', models.AutoField(primary_key=True, serialize=False)),
                ('doctorName', models.CharField(max_length=24, verbose_name='Doctor Name')),
                ('doctorUsername', models.CharField(max_length=15, verbose_name='Doctor Username')),
                ('doctorPass', models.CharField(max_length=100, verbose_name='Doctor Password')),
                ('doctorContact', models.IntegerField(verbose_name='Doctor Contact')),
                ('doctorEmail', models.EmailField(max_length=254, unique=True, verbose_name='Email Id')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_Id', models.AutoField(primary_key=True, serialize=False)),
                ('equipment_Name', models.CharField(max_length=50)),
                ('equipment_Quantity', models.IntegerField()),
                ('equipment_Assigned', models.IntegerField()),
                ('equipment_Usable', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Oxygen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oxygen_Total', models.IntegerField(help_text=' Days &')),
                ('oxygen_Total_Hour', models.TimeField(help_text=' Hours of Total Oxygen')),
                ('oxygen_Used', models.IntegerField(help_text=' Days &')),
                ('oxygen_Used_Hour', models.TimeField(help_text=' Hours of Oxygen Used')),
                ('oxygen_Remaining', models.IntegerField(help_text=' Days &')),
                ('oxygen_Remaining_Hour', models.TimeField(help_text=' Hours of Oxygen Remaining')),
            ],
        ),
        migrations.CreateModel(
            name='page',
            fields=[
                ('pageId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('content', tinymce.models.HTMLField()),
                ('status', models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled')], default='enabled', max_length=10)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('caseNumber', models.IntegerField(default=697478, unique=True, verbose_name='Case Number')),
                ('patientId', models.AutoField(primary_key=True, serialize=False)),
                ('patientName', models.CharField(max_length=24, verbose_name='Patient Name')),
                ('patientEmail', models.EmailField(max_length=254, unique=True, verbose_name='Email Id')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone', models.IntegerField(unique=True, validators=[home.models.validate_phoneNumber], verbose_name='Phone Number')),
                ('patientRelativeNumber', models.IntegerField(validators=[home.models.validate_phoneNumber], verbose_name="Relative's Phone number")),
                ('patientRelativeName', models.CharField(max_length=24, verbose_name="Relative's name")),
                ('line1', models.CharField(max_length=250, verbose_name='Address line1')),
                ('line2', models.CharField(max_length=250, verbose_name='Address line2')),
                ('pincode', models.IntegerField(validators=[home.models.validate_pincode], verbose_name='Pincode')),
                ('previousHistory', models.CharField(max_length=250, verbose_name='Previous history')),
                ('dob', models.DateField(verbose_name='Date of birth')),
                ('doctorNotes', models.CharField(blank=True, default=None, max_length=250, verbose_name='Doctor Notes')),
                ('doctorVisitingTime', models.DateTimeField(blank=True, default=None, verbose_name='Doctor Visiting Time')),
                ('dateTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Time')),
                ('patientStatus', models.CharField(choices=[('Pending', 'pending'), ('Critical', 'critical'), ('Recovering', 'recovering'), ('Recovered', 'recovered'), ('Deceased', 'deceased')], default='Pending', max_length=10, verbose_name='Patient Status')),
                ('bedNumber', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.bed')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.city')),
                ('doctorName', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('specializationId', models.AutoField(primary_key=True, serialize=False)),
                ('specialization', models.CharField(max_length=64, verbose_name='Specialization')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('staffId', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('staffUserName', models.CharField(default=None, max_length=24)),
                ('staffMiddleName', models.CharField(default=None, max_length=24)),
                ('staffLastName', models.CharField(default=None, max_length=24)),
                ('staffPassword', models.CharField(blank=True, max_length=24, null=True)),
                ('staffContactNumber', models.CharField(max_length=10)),
                ('staffEmail', models.EmailField(max_length=254, unique=True, verbose_name='Email Id')),
                ('staffPhoto', models.ImageField(blank=True, null=True, upload_to='staffImages')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('status', models.CharField(choices=[('active', 'Active'), ('on_leave', 'On_leave')], default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateId', models.AutoField(primary_key=True, serialize=False)),
                ('stateName', models.CharField(max_length=24, unique=True, verbose_name='State Name')),
            ],
        ),
        migrations.CreateModel(
            name='Symptoms',
            fields=[
                ('symptomsId', models.AutoField(primary_key=True, serialize=False)),
                ('symptoms', models.CharField(max_length=24, unique=True, verbose_name='Symptoms')),
                ('active', models.BooleanField(verbose_name='Active')),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('wardId', models.AutoField(primary_key=True, serialize=False)),
                ('wardName', models.CharField(max_length=10, verbose_name='Ward Name')),
                ('wardPrice', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ward Price')),
            ],
        ),
        migrations.CreateModel(
            name='WardDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorName', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.doctor')),
                ('wardName', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='home.ward')),
            ],
        ),
        migrations.CreateModel(
            name='PatientSymptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symptoms', models.ForeignKey(limit_choices_to={'active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.symptoms')),
                ('patientName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='', verbose_name='Document')),
                ('patientName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.state'),
        ),
        migrations.AddField(
            model_name='patient',
            name='wardName',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='home.ward'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.specialization'),
        ),
        migrations.AddField(
            model_name='city',
            name='stateName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.state'),
        ),
        migrations.AddField(
            model_name='bed',
            name='wardName',
            field=models.ForeignKey(default=None, max_length=5, on_delete=django.db.models.deletion.CASCADE, to='home.ward'),
        ),
    ]
