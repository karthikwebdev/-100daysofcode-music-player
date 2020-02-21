from pygame import mixer
def options():
    mixer.music.play()
    while True:
        print('1.set volume 2.pause 3.resume 4.stop')
        req = int(input('>>>'))
        if(req == 1):
            print('enter range from 0 - 1')
            sound = float(input('>>'))
            mixer.music.set_volume(sound)
        elif(req == 2):
            mixer.music.pause()
        elif(req == 3):
            mixer.music.unpause()
        elif(req == 4):
            mixer.music.stop()
            break
            
mixer.init() 
mixer.music.set_volume(0.7)


while True:
    print('enter which song to play....?')
    print('enter exit to quit')
    print('song1')
    print('song2')
    print('song3')
    req = input('>>>')
    if(req == 'song1'):
        mixer.music.load('song1.mp3')
        options()
    elif(req == 'song2'):
        mixer.music.load('song2.mp3')
        options()
    elif(req == 'song3'):
        mixer.music.load('song3.mp3')
        options()
    elif(req == 'exit'):
        break
    else:
        print('no such song...')
        
