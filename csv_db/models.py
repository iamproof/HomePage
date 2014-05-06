from django.db import models


class CountryList(models.Model):
	Common_Name = models.CharField(max_length=50)
	Formal_Name = models.CharField(max_length=50)
	Type = models.CharField(max_length=50, default=None)
	Sub_Type = models.CharField(max_length=50, default=None)
	Sovereignty = models.CharField(max_length=50, default=None)
	Capital = models.CharField(max_length=50, default=None)
	Currency_Code = models.CharField(max_length=50, default=None)
	Currency_Name = models.CharField(max_length=50, default=None)
	Telephone_Code = models.CharField(max_length=10, default=None)
	Letter_Code = models.CharField(max_length=10, default=None)
	ISO_Number = models.CharField(max_length=10, default=None)
	Country_Code_TLD = models.CharField(max_length=5, default=None)

	def __str__(self):
		return self.Common_Name