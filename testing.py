
data = {
    'shkhaider': 
    {
        'user': ('shkhaider, shkhaider2015@gmail.com, 7b3c7b90e070d6fe.jpg'),
         'post': 16
    },
    'dawoodhaider': 
    {
        'user': ('dawoodhaider, dawoodhaider@gmail.com, gdfgdfgdfgfd.jpg'),
         'post': 13
    }
}

for a in data.values():
    for b in a.values():
        print(b)