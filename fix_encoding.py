paths= ["/data/data/com.termux/files/home/bot/EchoRP-READMe.md","/data/data/com.termux/files/home/bot/F-tr.Readme.md"]
for path in paths:
    with open(path,"r",encoding="cp1251") as f:
        text = f.read()

    with open(path,"w",encoding="utf-8") as f:
        f.write(text)

    print(f"Готово:{path}")

