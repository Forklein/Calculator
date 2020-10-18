nome = input('Ciao!, inserisci il tuo nome: ')
print ('Ciao ' + nome + '! Questo è il bot calculator di Peppe')
numero = float(input('Inserisci il primo numero: '))
op = input('Inserisci operatore: ')
numeroo = float(input('Inserisci il secondo numero: '))
if op == '+':
 print(numero+numeroo)
elif op == '-':
 print(numero-numeroo)
elif op == '*':
 print(numero*numeroo)
elif op == '/':
 print(numero/numeroo)
else:
 print('Hai inserito un operatore non corretto')
