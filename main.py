import pyautogui
import time

groups = [
    100063131419572, # დაჩი საზანდრიშვილი
    100090728942101, # ჯეკო ტარიელაძე
    100085580697915, # ნოდო ცინცაძე
    61550499584452, # გიორგი თაკაშვილი
    100085446177130, # კოსტა კოსტანიანი
    100035671861454, # ლუკა სიჭინავა
    100026218537993, # გიორგი ჯოხაშვილი
    100088713196091, # ზაზა ბორისოვი
    100090173277690, # დათო გაფრინდაშვილი
    100050910513088, # გიგა ყიფიანი
    100063423801739, # დემეტრე სამხარაძე 
    100082679139866, # ანდრია აბულაძე
    100069832299716, # სანდრო ჯალაღონია
    # რატი
    # გეგა
    100089057330630, # ნიკოლოზ ჟუჟუნაძე
    100037308340350, # ლუკა გიორიგაძე
    # დმეტრე 
    # გიორგი
    100087006662871, # ელენე მახარაძე
    61551312504843, # თათული ბოჟაძე
    61551306507657, # ნინი ლობჟანიძე
    61550835587181, # ილია ლობჟანიძე
    # ალექს რაჟივი
    100055285411613, # გოგა ბოლქვაძე
    100055435190692, # მათე ეგრისელაშვილი
    100048711770555, # გიორგი ამირაძე
    100009183564970, # რეზი ჯგუშია
    100010951717720, # მარიამ სურმანიძე
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
    print(link)
    pyautogui.typewrite(link)
    pyautogui.typewrite('\n')

    print("Waiting for 45 seconds\n")
    time.sleep(30)

    pyautogui.typewrite('p')
    time.sleep(2)
    print("Writing post\n")
    pyautogui.typewrite("miuxedavad imisa rom chatshi davwere mainc shegaxsenebt dges 9 saatze gvaqvs patara masterklasi discord-ze. viqnebit grdzelo-voice shi <3")
    time.sleep(4)

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')

    time.sleep(3)

    pyautogui.write(['f6'])
    time.sleep(1)
print('End of taks')
