# coding=utf-8

from Camera_happyNewYear import Camera

print "-----카메라의 현재 모드를 보여줍니다-----"
Nikon = Camera()
print Nikon.currentMode()

print "-----카메라의 플래쉬를 끕니다-----"
Nikon.flashOff()
print Nikon.flash

print "-----타이머를 작동시켜 카메라를 촬영합니다.-----"
Nikon.setTimer(10)
print Nikon.getTimer()
print Nikon.shutter()
print Nikon.timer


print "---타이머를 작동시켜 동영상을 촬영합니다.-----"
Nikon.setTimer(3)
print Nikon.setMode(2)
print Nikon.getTimer()
print Nikon.shutter()

print "---조리개를 조절하여 촬영합니다.-----"
print Nikon.iris
Nikon.setIris(0.25)
print Nikon.iris
print Nikon.shutter()