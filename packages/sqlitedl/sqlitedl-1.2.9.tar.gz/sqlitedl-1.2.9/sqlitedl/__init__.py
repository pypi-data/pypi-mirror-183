import sqlite3

class create:
	def __init__(self, file):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
		else: raise NameError(f'Invalid file: {file}')
	def db(self, name, key, settings):
		self.c.execute(f'''CREATE TABLE {name}
			({key} PRIMARY KEY, {settings})''')
	def line(self, name, variable, values):
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
class update:
	def __init__(self, file, name, key):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
			self.name = name
			self.key = key
		else: raise NameError(f'Invalid file: {file}')
	def intvar(self, key, variable, mode, change):
		if mode == 'set':
			self.c.execute(f'UPDATE {self.name} SET {variable} = ? WHERE {self.key} = ?', (change, key))
		elif mode in ('*', '/', '+', '-'):
			self.c.execute(f'UPDATE {self.name} SET {variable} = {variable} {mode} ? WHERE {self.key} = ?', (change, key))
		else:
			raise ValueError(f'invalid mode: {mode}')
		self.conn.commit()
	def charvar(self, key, variable, change):
		self.c.execute(f'UPDATE {self.name} SET {variable} = ? WHERE {self.key} = ?', (change, key))
		self.conn.commit()
class get:
	def __init__(self, file, name):
		if file.endswith('.db'):
			self.conn = sqlite3.connect(file)
			self.c = self.conn.cursor()
			self.name = name
		else: raise NameError(f'Invalid file: {file}')
	def line(self, key, key_value):
		return self.c.execute(f'SELECT * FROM {self.name} WHERE {key} = ?', (key_value, )).fetchone()
