# coding=utf-8
####Camera 클래스

class Camera:
    mode = {1: "picture", 2: "video", 3: "panoram", 4: "slomo"}
    currentmode = "picture"
    flash = True
    hdr = True
    timer = 0
    iris = 0.0078125


    def currentMode(self):
        return self.currentmode

    # flashOn() : flash의 상태를 on로 바꿔줍니다
    def flashOn(self):
        self.flash = True
        return self.flash

    # flashOn() : flash의 상태를 off로 바꿔줍니다
    def flashOff(self):
        self.flash = False
        return self.flash

    # hderOn() : hdr의 상태를 on로 바꿔줍니다
    def hdrOn(self):
        self.hdr = True
        return self.hdr

    # hdrOn() : hdr의 상태를 off로 바꿔줍니다
    def hdrOff(self):
        self.hdr = False
        return self.hdr


    def setTimer(self, sec):
        self.timer = sec

    def getTimer(self):
        return self.timer

    def setMode(self, mode):

        if mode > 4:
            return "해당 모드를 지원하지 않습니다"

        self.currentMode = self.mode[mode]

    def shutter(self):
        if self.timer == 0:
            return "%s를 찍습니다" % self.currentMode
        if self.timer > 0:
            for i in range(self.timer, -1, -1):
                print "%s초 남았습니다" % i
            self.timer = 0
            return "%s를 촬영합니다" % self.currentMode

        else:
            return "타이머 오류입니다"


    def setIris(self, stop):
        self.iris = stop
        return self.iris