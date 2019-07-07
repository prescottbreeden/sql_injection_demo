import sqlite3

# query = "CREATE TABLE user (username TEXT, password TEXT);"
# query = "INSERT INTO user (username, password) VALUES (?,?);"
# users = [
#     ('Bob', '12345'),
#     ('Kate', 'ald_kfj$%hal43dfk_--jlh'),
#     ('Steve', 'meow'),
# ]

u = input("please enter your username...")
p = input("please enter your password...")
bad_query = "SELECT * FROM user WHERE username='%s' AND password='%s'" % (u, p)
good_query = "SELECT * FROM user WHERE username=? AND password=?"

# Injection
# "SELECT * FROM user WHERE username='Sprinkles' AND passowrd='' OR 1=1 --'"

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute(bad_query)
# c.execute(bad_query, (u, p))
result = c.fetchone()
if result:
    print("*"*80)
    print('     Welcome Back!')
    print("*"*80)
else:
    print("!"*80)
    print('     Password is Invalid!')
    print("!"*80)

conn.commit()
conn.close()
