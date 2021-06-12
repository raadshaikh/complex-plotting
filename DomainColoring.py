from PIL import Image
import colorsys
import math
import cmath

def coordconv(x,y,width,height):
	return (width/2 + x, height/2 - y -1)

lumdropoff=1.07

def z2rgb(z):
	x=z.real
	y=z.imag
	modz=(x**2 + y**2)**0.5
	lum=(1 - lumdropoff**(-modz))
	hue=math.atan2(y,x)/(2*math.pi)
	rgb_norm=colorsys.hls_to_rgb(hue, lum, 1)
	return (int(rgb_norm[0]*255), int(rgb_norm[1]*255), int(rgb_norm[2]*255))

scale=10 #scale/zoom factor
(width, height)=(256, 256)
j=complex(0,1)

do=Image.new('RGB', (width, height))#do for domain
dopixels=do.load()

for x in range(-int(width/2),int(width/2)):
	for y in range(-int(height/2),int(height/2)):
		z_unscaled=complex(x, y)
		z=z_unscaled/scale
		w=z
		dopixels[coordconv(x,y,width,height)[0],coordconv(x,y,width,height)[1]]=(z2rgb(w)[0],z2rgb(w)[1],z2rgb(w)[2])
print("Domain rendered.")

im=Image.new('RGB', (width, height))
impixels=im.load()

for x in range(-int(width/2),int(width/2)):
	for y in range(-int(height/2),int(height/2)):
		z_unscaled=complex(x, y)
		z=z_unscaled/scale
		try:
		    w=-10*cmath.log(1-z)/z
		    #w=cmath.log(z)+cmath.log(z-10)
		    #w=(z**2 - 1)**(1/2)
		    #w=5*(math.e**(z*j/10) + math.e**(-z*j/10)) #Put your function w=f(z) here
		    impixels[coordconv(x,y,width,height)[0],coordconv(x,y,width,height)[1]]=(z2rgb(w)[0],z2rgb(w)[1],z2rgb(w)[2])
		except (ZeroDivisionError, ValueError):
		    	impixels[coordconv(x,y,width,height)[0],coordconv(x,y,width,height)[1]]=(255,255,255)
		
print("\nImage rendered.")

tot=Image.new('RGB', (int(2.03*width), height))
tot.paste(do, (0,0))
tot.paste(im, (int(1.03*width), 0))

tot.save("output.png")

print("\nConcatenated render saved.")