from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImagenForm
from .models import imagen
from subprocess import *
import sys
import csv

# Create your views here.
def index(request):
	if request.method == 'POST':
		formImagen = ImagenForm(request.POST, request.FILES)
		print('normal')
		if (formImagen.is_valid()):
			print('post fake')
			imagen_obj = formImagen.save()
			imagen_obj.foto = request.FILES.get('foto', False)
			test_path = imagen_obj.foto.url
			output_path = "outout"
			current = "/home/mila/Downloads/ICR/"
			print("maybe")
			call(["cat", "/home/mila/Downloads/ICR/miau.txt"])
			print("maybe2")
			print(test_path)
			print(imagen_obj.foto.name)
			img_dir = "static/media/images/"
			out_dir = "static/media/output/"
			call(["sudo", "tesseract", img_dir + imagen_obj.foto.name, out_dir + output_path, "-l", "icr", "--tessdata-dir", "static/media/tessdata/"])
			print("before")
			with open(out_dir + output_path+".txt") as f:
				data = f.readlines()
			print("here")
			reader = csv.reader(data)
			result = ''
			ans = ''
			for row in reader:
				print(row)
				ans = ans + result.join(row) + '\n'
			print(ans)
			imagen_obj.resultado = ans
			imagen_obj.save()
			return redirect('/result/' + str(imagen_obj.id) + '/')	
	else:
		print('no post')
		return render(request, 'ICR.html')	
	return render(request, 'ICR.html')

def mostrar_resultado(request, idImagen):
	try:
		img = imagen.objects.get(id=idImagen)
		contexto = {'image': img}
		print('en el try')
		return render(request, 'ICRresult.html',contexto)
		print('en el try aun')
	except imagen.DoesNotExist:
		img = None
		return render(request, 'ICRresult.html', {'image', img})
