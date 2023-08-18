margem_lucro = 0.27

print(f"Margem: {margem_lucro:.1%}")


from datetime import datetime

hoje = datetime.now()
print(f"Data: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")