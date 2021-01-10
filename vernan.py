#!/usr/bin/env	python
#Biblioteca	sys:	Requisito	para	a	passagem	de	parâmetros	na	linha	de	comando
import	sys, binascii
#Biblioteca	usada	para	transformar	uma	string	em	hexadecimal	e	vice-versa

#Armazenará	a	palavra-secreta
key	= sys.argv[2]

#Armazenará	o	modo	de	operação
mode = sys.argv[3]

#Armazenará	a	posição	de	uma	letra	da	palavra-secreta
keyidx	=	0

#Resuldado
xored	=	''

#Esse	if	transforma	o	argumento	recebido	em	hexadecimal	caso	o	modo	de	operação	seja	decriptografia
if	mode ==	'enc':
    msg	= sys.argv[1]
elif	mode ==	'dec':
    msg	= binascii.unhexlify(sys.argv[1])

#Esse	for	executa	uma	vez	para	cada caractere	da	mensagem
for	msgchar	in	msg:
    
    #Essa	linha	faz	a	operação	XOR:
    #chr()	– transforma	um	caractere	em	decimal	para	ascii
    #ord()	– transforma	um	caractere	ascii	em	decimal
    xored += chr(ord(key[keyidx%len(key)])	^	ord(msgchar))
   
    #Controla	qual	letra	da	palavra-secreta	será	usada	na	próxima	iteração	for
    keyidx += 1

    #Esse	if	transforma	o	resultado	em	hexadecimal	caso	o	modo	de	operação	seja	encriptação
if	mode ==	'enc':
    print	binascii.hexlify(xored)
elif	mode ==	'dec':
    print	xored
