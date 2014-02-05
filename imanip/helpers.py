from PIL import Image, ImageFilter, ImageEnhance
from random import randint

def name_gen(pathname):
	rand_prefix = str(randint(100, 99999999))
	return rand_prefix + pathname

def grayscale(path, level):
	img = Image.open(path).convert('L').save(path)

def brightness(path, level=1.5):
	img = Image.open(path).convert('RGB')
	enhancer = ImageEnhance.Brightness(img)
	enhancer.enhance(level).save(path)

def contrast(path, level=1.5):
	img = Image.open(path).convert('RGB')
	enhancer = ImageEnhance.Contrast(img)
	enhancer.enhance(level).save(path)

def red_level(path, level=1):
	level = level - 1
	img = Image.open(path).convert('RGB')
	source = img.split()
	r = 0
	r_out = source[r].point(lambda i: i + (255 * level))
	source[r].paste(r_out)
	img = Image.merge('RGB', source)
	img.save(path)

def green_level(path, level=1):
	level = level - 1
	img = Image.open(path).convert('RGB')
	source = img.split()
	g = 1
	g_out = source[g].point(lambda i: i + (255 * level))
	source[g].paste(g_out)
	img = Image.merge('RGB', source)
	img.save(path)

def blue_level(path, level=1):
	level = level - 1
	img = Image.open(path).convert('RGB')
	source = img.split()
	b = 2
	b_out = source[b].point(lambda i: i + (255 * level))
	source[b].paste(b_out)
	img = Image.merge('RGB', source)
	img.save(path)

def sepia(path, level=1.5):
	img = Image.open(path).convert('RGB')
	source = img.split()
	r, g, b = 0, 1, 2
	r_sep, g_sep, b_sep = 112, 66, 20
	r_out = source[r].point(lambda i: ((i * (2 - level)) + (r_sep * level)) / 2)
	g_out = source[g].point(lambda i: ((i * (2 - level)) + (g_sep * level)) / 2)
	b_out = source[b].point(lambda i: ((i * (2 - level)) + (b_sep * level)) / 2)
	source[r].paste(r_out)
	source[g].paste(g_out)
	source[b].paste(b_out)
	img = Image.merge('RGB', source)
	img.save(path)

def quantize(path, level):
	colors = int(level * 4) + 2
	img = Image.open(path).convert('RGB')
	q = img.quantize(colors=colors).convert('RGB')
	q.save(path)

def bitify(path, level):
	img = Image.open(path).convert('RGB')
	size = img.size
	scale = int(level * 8) + 1
	small = img.resize((size[0]/scale, size[1]/scale))
	big = small.resize((size[0], size[1]))
	q = big.quantize(colors=128).convert('RGB')
	q.save(path)

def edge_detect(path, level):
	img = Image.open(path).convert('RGB')
	img = img.filter(ImageFilter.FIND_EDGES)
	img.save(path)

effect_list = {
		'grayscale': grayscale
	,	'brightness': brightness
	,	'contrast': contrast
	, 'red_level': red_level
	, 'green_level': green_level
	, 'blue_level': blue_level
	,	'sepia': sepia
	,	'quantize': quantize
	,	'bitify': bitify
	,	'edge_detect': edge_detect
}

def apply(path, effects):
	for i in effects:
		print i
		effect = str(i['effect_name'])
		print effect
		val = float(i['value'])/100
		effect_list[effect](path, val)