from PyQt5.QtCore import QThread


# 用于线程操作
#
class Run_Thread(QThread):
    def __init__(self, parent=None):
        super(QThread, self).__init__(parent)
        self.Filepath = ''
        self.backTimes = 1

    def run(self):
        if self.Filepath != '':
            import action.Output as output
            # output.wait_start()
            for i in range(self.backTimes):
                output.startAction(self.Filepath)

    def recode(self):
        if self.Filepath != '':
            import action.Listening as rd
            rd.sumScript(self.Filepath)

    def stop(self):
        self._running = False
        self.wait()  # 等待线程结束
