import sqlite3

class create:
	def __init__(self, file):
		self.conn = sqlite3.connect(file)
		self.c = self.conn.cursor()
	def db(self, name, key, settings):
		self.c.execute(f'''CREATE TABLE IF NOT EXISTS {name}
			({key} INTEGER PRIMARY KEY, {settings})''')
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
		self.conn = sqlite3.connect(file)
		self.c = self.conn.cursor()
		self.name = name
		self.key = key
	def intvar(self, key, variable, mode, change):
		if mode == '+':
			self.c.execute(f'UPDATE {self.name} SET {variable} += ? WHERE {self.key} = ?', (change, key))
			self.conn.commit()
		elif mode == '-':
			self.c.execute(f'UPDATE {self.name} SET {variable} -= ? WHERE {self.key} = ?', (change, key))
			self.conn.commit()
		elif mode == '/':
			self.c.execute(f'UPDATE {self.name} SET {variable} = {variable} / ? WHERE {self.key} = ?', (change, key))
			self.conn.commit()
		elif mode == '*':
			self.c.execute(f'UPDATE {self.name} SET {variable} = {variable} * ? WHERE {self.key} = ?', (change, key))
			self.conn.commit()
		elif mode == 'set':
            self.c.execute(f'UPDATE {self.name} SET {variable} = ? WHERE {self.key} = ?', (change, key))
			self.conn.commit()
	def charvar(self, key, variable, change):
		self.c.execute(f'UPDATE {self.name} SET {variable} = ? WHERE {self.key} = ?', (change, key))
		self.conn.commit()
class get:
	def __init__(self, file, name):
		self.conn = sqlite3.connect(file)
		self.c = self.conn.cursor()
		self.name = name
	def line(self, key, key_value):
		return self.c.execute(f'SELECT * FROM {self.name} WHERE {key} = ?', (key_value, )).fetchone()
