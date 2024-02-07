

from tqdm import tqdm
loop = tqdm(total=5000, position=0, leave=False)
for k in range (5000):
    loop.set_description("Loading...".format(k))
    loop.update(1)



from tqdm.auto import tqdm
for i in tqdm(range(100001)):
    print("",end="\r")
