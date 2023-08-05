import sqlite3
def assert_type(var, name, types):
	if type(var) != types:
		raise ValueError(f'invalid type: {name} is not {types} but {type(var)}')
class create:
	def __init__(self, file):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
		else: raise NameError(f'Invalid file: {file}')
	def db(self, name, key, variables):
		assert_type(name, 'TableName', str)
		assert_type(key, 'KeyName', str)
		assert_type(variables, 'variables', str)
		if name == '': raise ValueError('TableName is empty!')
		if key == '': raise ValueError('KeyName is empty!')
		if variables == '': raise ValueError('variables is empty!')
		self.c.execute(f'''CREATE TABLE {name}
			({key} PRIMARY KEY, {variables})''')
	def line(self, name, variable, values):
		assert_type(name, 'TableName', str)
		assert_type(variable, 'variable', str)
		if name == '': raise ValueError('TableName is empty!')
		if variable == '': raise ValueError('variable is empty!')
		args = variable.split(', ')
		val = ''
		for i in range(len(args)):
			val += '?'
			if (i+1) == len(args):
				pass
			else:
				val += ', '
		self.c.execute(f'INSERT INTO {name} ({variable}) VALUES ({val})', values)
		self.conn.commit()
class Reference:
	def __init__(self, update_ref, key_value, variable_name):
		self.update_ref = update_ref
		self.key_val = key_value
		self.var = variable_name
	def variable_type(self):
		var = self.update_ref.c.execute(f'SELECT {self.var} FROM {self.update_ref.table_name} WHERE {self.update_ref.key} = ?', (self.key_val, )).fetchone()
		if var is None: raise ValueError(f'{self.var} is NoneType!')
		return type(var[0])
	def updatevalue(self, oper, change):
		assert_type(change, 'change', self.variable_type())
		if change is None: raise ValueError(f'change is NoneType!')
		if oper in ('*', '+', '/', '-'):
			self.update_ref.c.execute(f'UPDATE {self.update_ref.table_name} SET {self.var} = {self.var} {oper} ? WHERE {self.update_ref.key} = ?', (change, self.key_val))
		elif oper == 'set':
			self.update_ref.c.execute(f'UPDATE {self.update_ref.table_name} SET {self.var} = ? WHERE {self.update_ref.key} = ?', (change, self.key_val))
		else: raise ValueError(f'Operation is valid!')
		self.update_ref.conn.commit()
	def add(self, change):
		self.updatevalue('+', change)
	def sub(self, change):
		self.updatevalue('-', change)
	def mult(self, multiply):
		self.updatevalue('*', multiply)
	def div(self, divider):
		self.updatevalue('/', divider)
	def set(self, value):
		self.updatevalue('set', value)
class update:
	def __init__(self, file, table_name, key):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
			self.table_name = table_name
			self.key = key
		else: raise NameError(f'Invalid file: {file}')
	def var(self, key_value, variable_name):
		return Reference(self, key_value, variable_name)
class get:
	def __init__(self, file, name):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
			self.name = name
		else: raise NameError(f'Invalid file: {file}')
	def line(self, key, key_value):
		assert_type(key, 'key', str)
		assert_type(key, 'key_value', str)
		return self.c.execute(f'SELECT * FROM {self.name} WHERE {key} = ?', (key_value, )).fetchone()
