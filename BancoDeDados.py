import sqlite3

conn = sqlite3.connect('UsuariosApp.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")

print('Conectando ao Banco de Dados')