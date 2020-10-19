nome = input('Ciao!, inserisci il tuo nome: ')
print('Ciao ' + nome + '! Questo è il bot calculator di Peppe')
numero = float(input('Inserisci il primo numero: '))
numeroo = float(input('Inserisci il secondo numero: '))
gang = True
while gang == True:
 op = input('Inserisci operatore: ')
 if op == '+':
     print('Il risultato è: ', end ='')
     print(numero+numeroo)
     break
 elif op == '-':
     print('Il risultato è: ', end ='')
     print(numero-numeroo)
     break
 elif op == '*':
     print('Il risultato è: ', end ='')
     print(numero*numeroo)
     break
 elif op == '/':
     print('Il risultato è: ', end ='')
     print(numero/numeroo)
     break
 else:
     print('Hai inserito un operatore non corretto, riprova!')
     continue
