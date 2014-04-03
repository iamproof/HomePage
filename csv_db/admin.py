from django.contrib import admin
from csv_db.models import CountryList


class CountryListAdmin(admin.ModelAdmin):
	fields = ['Common_Name','Formal_Name','Type', 'Sub_Type', 'Sovereignty',
			  'Capital', 'Currency_Code', 'Currency_Name', 'Telephone_Code',
			  'Letter_Code', 'ISO_Number','Country_Code_TLD']
	list_display = ('Common_Name', 'Currency_Name', 'Capital')
	list_filter = ['Currency_Name']

admin.site.register(CountryList, CountryListAdmin)