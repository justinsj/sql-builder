# DomainSpecificSQLBuilder.py

from AdvancedSQLBuilder import AdvancedSQLBuilder
class DomainSpecificSQLBuilder(AdvancedSQLBuilder):
    def CARNAME(self, name, table_two, key_two):
        self.JOIN("CAR_MAP","ID", table_two, key_two)
        self.AND(f"CAR_MAP.NAME = {name}")
        return self
    