# SQLBuilder.py

newline = "\n"

class SQLBuilder(object):
	def __init__(self):
		self._DECLARE = ""
		self._SELECT = ""
		self._FROM_MAP = {}
		self._WHERE = ""
		self._ORDER_BY = ""
		self._GROUP_BY = ""
		self._HAVING = ""
	
	
	def DECLARE(self, key, type, value = ''):
		assert(key.startswith('@'))
		
		# Handle keyword starting with declare
		s = "\n"
		if (self._DECLARE == ""):
			s = ""
		
		self._DECLARE += s + f"DECLARE {key} {type}{' = ' if value else ''}{value}"
		return self
	def SELECT(self, t):
		s = ", "
		if (self._SELECT == ""):
			s = "SELECT "
		
		self._SELECT += s + t
		return self
	
	def FROM(self, t, alias=''):
		if (not t in self._FROM_MAP):
			self._FROM_MAP[t] = ''

		if (alias): 
			self._FROM_MAP[t] = alias

		return self
	def WHERE(self, t):
		if (self._WHERE != ""):
			return self.AND(t)
		self._WHERE = "WHERE " + t
		return self
		
	def AND(self, t):
		s = "\n"
		if (self._WHERE == ""):
			s = "WHERE 1=1\n"
		
		self._WHERE += s + f"AND {t}"
		return self
	
	def GROUP_BY(self, t):
		s = ",\n"
		if (self._GROUP_BY == ""):
			s = "GROUP BY "
		
		self._GROUP_BY += s + t
		return self
	
	def ORDER_BY(self, t):
		s = ",\n"
		if (self._ORDER_BY == ""):
			s = "ORDER BY "
		
		self._ORDER_BY += s + t
		return self
	
	def HAVING(self, t):
		s = ",\n"
		if (self._HAVING == ""):
			s = "HAVING "
		
		self._HAVING += s + t
		return self
	def JOIN(self, table_one, key_one, table_two, key_two):
		return self.FROM(table_one).FROM(table_two).AND(f"{table_one}.{key_one} = {table_two}.{key_two}")
	
	def BUILD(self):
		self._FROM = ', '.join([f"{name}{f' {alias}' if alias else ''}" for name, alias in self._FROM_MAP.items()])
		return (
			f"{self._DECLARE + newline if self._DECLARE else ''}"
			+ f"{newline + self._SELECT if self._SELECT else ''}"
			+ f"{newline + 'FROM ' + self._FROM if self._FROM else ''}"
			+ f"{newline + self._WHERE if self._WHERE else ''}"
			+ f"{newline + self._GROUP_BY if self._GROUP_BY else ''}"
			+ f"{newline + self._HAVING if self._HAVING else ''}"
			+ f"{newline + self._ORDER_BY if self._ORDER_BY else ''}"
		)