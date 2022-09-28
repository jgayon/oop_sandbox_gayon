# %%
from media_loader2 import MediaLoader, Wav, Ogg


#%%
# It is not possible to create objects from abstract class
#media = MediaLoader()

# %%
# If a child class does not implement required methods and attributes 
# you cannot instantiaste an object from it
#wav = Wav()

# %%
ogg = Ogg()
ogg.play()

ogg.ext = ".mp3"
print(ogg.ext)