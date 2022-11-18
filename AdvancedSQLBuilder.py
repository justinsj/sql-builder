# AdvancedSQLBuilder.py

from SQLBuilder import SQLBuilder

class AdvancedSQLBuilder(SQLBuilder):
	def HOURS(self, key, n):
		assert(n > 0)
		
		self.AND(f"{key} >= DATEADD(HOUR, -{n}, GETDATE())")
		return self

	def TODAY(self, key):
		self.AND(f"CONVERT(VARCHAR(10), {key}, 102) = CONVERT(VARCHAR(10), GETDATE(), 102)")
		return self
	
	def START_DATE(self, key, start_date):
		(self.DECLARE('@start_date','datetime',start_date)
			.AND(f"{key} is not null")
			.AND(f"{key} >= @start_date"))
		return self
	
	def END_DATE(self, key, end_date):
		self.DECLARE('@end_date','datetime',end_date)
		self.AND(f"{key} is not null")
		self.AND(f"{key} < @end_date")
		return self
	
	def LIKE(self, key, s):
		self.AND(f"{key} like '{s}'")
		return self

	def NULL(self, key):
		self.AND(f"{key} is null")
		return self
	
	def NOTNULL(self, key):
		self.AND(f"{key} is not null")
		return self