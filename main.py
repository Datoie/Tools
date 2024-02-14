import pyautogui
import time
groups = [

    # 100085580697915, # ნოდო ცინცაძე
    # 61550499584452, # გიორგი თაკაშვილი
    # 100085446177130, # კოსტა კოსტანიანი
    # 100035671861454, # ლუკა სიჭინავა
    # 100026218537993, # გიორგი ჯოხაშძე
    # 100088713196091, # ზაზა ბორისოვი
    # 100090173277690, # დათო გაფრინდაშვილი
    # 100050910513088, # გიგა ყიფიანი
    # 100063423801739, # დემეტრე სამხარაძე 
    # 100069832299716, # სანდრო ჯალაღონია
    100089057330630, # ნიკოლოზ ჟუჟუნაძე
    100037308340350, # ლუკა გიორიგაძე
    # დმეტრე    
    # გიორგი
    # ლასშა
    100087006662871, # ელენე მახარაძე
    61551312504843, # თათული ბოჟაძე   
    # ალექს რაჟივი
    # 100055285411613, # გოგა ბოლქვაძე
    100055435190692, # მათე ეგრისელაშვილი
    61555762035585, # მარიამ რაზმაძე
    100082190902319, # ალექსანდრე ბადურაშვილი
    # 61556310694877, # დაჩი შურგულია
    100080954673821, # ნოდარ ძამუნაშვილი
    100048711770555, # გიორგი ამირაძე
    100032780054804, # უჩა კუბერიშვილი
    100069011828281, # მათე ბერიძე
    # 100010951717720, # მარიამ სურმანიძე
    100072521763126, # დაჩი თავაძე
    100068348285662, # ირაკლი მახარაძე
    100009183564970, # რეზი ჯგუშია
    # 100093532583327, # ბარბარე დიასამიძ
    1000077163821451 # მაინ ფერსონ
    ]

time.sleep(5)

pyautogui.keyDown('alt')
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyUp('alt')


pyautogui.keyDown('ctrl')
pyautogui.keyDown('t')
pyautogui.keyUp('t')
pyautogui.keyUp('ctrl')


for i in range(len(groups)):
    link = 'https://www.facebook.com/messages/t/'+ str(groups[i])
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')
    print("Waiting for 45 seconds\n")
    time.sleep(5)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("გამარჯობა მეილი ჩამიგდე თუ შეძლება <3     <3")
    
    pyautogui.typewrite("")
    time.sleep(4)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)


    pyautogui.write(['f6'])
    time.sleep(1)
print('End of taks')
