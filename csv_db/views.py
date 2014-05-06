from django.shortcuts import render
from csv_db.models import CountryList
import csv
from django.http import HttpResponse
import os


def import_csv_file():
	path = os.getcwd()+"/csv_db/countrylist.csv"
	with open(path) as plik:
		country_list = csv.reader(plik)
		country_list = [i for i in country_list]
		country_list = country_list[1:]

	for row in country_list:
		db_obj = CountryList(
			Common_Name = row[1],
			Formal_Name = row[2],
			Type = row[3],
			Sub_Type = row[4],
			Sovereignty = row[5],
			Capital = row[6],
			Currency_Code = row[7],
			Currency_Name = row[8],
			Telephone_Code = row[9],
			Letter_Code = row[11],
			ISO_Number = row[12],
			Country_Code_TLD = row[13],
			)
		db_obj.save()


def index(request):
	full_list = CountryList.objects.all()
	return render(request, "csv_db/index.html", {'full_list': full_list})

def order(request, order_item):
	full_list = CountryList.objects.order_by(order_item)
	if "-" in order_item:
		return render(request, "csv_db/decreasing_order.html", {'full_list': full_list})
	return render(request, "csv_db/increasing_order.html", {'full_list': full_list})


def csv_file(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
	writer = csv.writer(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
	# quoting option: csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE

	country_list = CountryList.objects.all()
	writer.writerow(["Common_Name", "Formal_Name", "Type", "Sub_Type", "Sovereignty",
					 "Capital", "Currency_Code", "Currency_Name", "Telephone_Code",
					 "Letter_Code", "ISO_Number", "Country_Code_TLD"])
	for country in country_list:
		writer.writerow([country.Common_Name,
						 country.Formal_Name,
						 country.Type,
						 country.Sub_Type,
						 country.Sovereignty,
						 country.Capital,
						 country.Currency_Code,
						 country.Currency_Name,
						 country.Telephone_Code,
						 country.Letter_Code,
						 country.ISO_Number,
						 country.Country_Code_TLD])
	return response