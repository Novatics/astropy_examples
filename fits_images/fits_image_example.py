import matplotlib.pyplot as plt

from astropy.visualization import astropy_mpl_style
from astropy.utils.data import download_file
from astropy.io import fits

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True)

fits.info(image_file)

image_data = fits.getdata(image_file, ext=0)
print(image_data.shape)

plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()