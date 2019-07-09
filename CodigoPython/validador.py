#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

def validor_email(email):
	if(len(email) > 7):
		return bool(re.match("^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$",email.lower()))


if (validor_email(raw_input("Ingresa correo electrónico: "))):
	print("Correo válido")
else:
	print("Correo inválido")
