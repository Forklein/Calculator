from getch import pause
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
     pause('Premi un tasto per terminare')
     break
 elif op == '-':
     print('Il risultato è: ', end ='')
     print(numero-numeroo)
     pause('Premi un tasto per terminare')
     break
 elif op == '*':
     print('Il risultato è: ', end ='')
     print(numero*numeroo)
     pause('Premi un tasto per terminare')
     break
 elif op == '/':
     if numeroo == 0:
             print('Errore, un numero non è divisibile per zero')
             pause('Premi un tasto per terminare')
             break
     else:
         print('Il risultato è: ', end ='')
         print(numero/numeroo)
         pause('Premi un tasto per terminare')
         break
 else:
     print('Hai inserito un operatore non corretto, riprova!')
     continue
