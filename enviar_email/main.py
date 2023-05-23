import win32com.client as win32

# Criar a integração com o outlook
outlook = win32.Dispatch('outlook.application')

# Criar um emal
email = outlook.CreateItem(0)

# Configurar as informações do seu e-mal

email.To = 'angelo.carnevale@hotmail.com'
email.Subject = 'E-mail automático do Python'
email.HTMLBody = """
<p>Testando</p>

<p>Saudações / Best re</p>
"""

email.Send()
print("Email enviado")
