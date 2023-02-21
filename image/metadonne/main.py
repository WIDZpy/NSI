import PIL.Image


def convertion(exif_dict: dict) -> tuple[float, float]:
	"""
	: param exif_dict : les donner exif d'une image
	: return : les coordoné en degré décimal ou a été prise la photo
	"""
	assert 34853 in exif_dict, "pas de cordooné gps"

	gps = exif_dict[34853]

	signe = -1 if gps[1] == "S" else 1, -1 if gps[3] == "W" else 1

	dd = float(gps[2][0] + gps[2][1]/60 + gps[2][2]/360), float(gps[4][0] + gps[4][1]/60 + gps[4][2]/3600)

	return signe[0] * dd[0], signe[1] * dd[1]


def main():

	img = PIL.Image.open("liberty.jpg")
	exif = img._getexif()
	print(convertion(exif))


if __name__ == '__main__':
	main()

