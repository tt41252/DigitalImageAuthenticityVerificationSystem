import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# 导入你由 Qt Designer 自动生成的界面类
from main_1 import Ui_MainWindow 

class MyLogicWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 1. 初始化 UI 界面
        self.setupUi(self)
        
        # 2. 调用绑定信号与槽的函数
        self.bind_signals()

    def bind_signals(self):
        """
        将界面的按钮点击信号（clicked）连接到显示文字的槽函数上。
        根据你提供的 main_1.py，控件名称已经完美匹配。
        """
        # ================== 图像真实性鉴定 ==================
        self.pushButton.clicked.connect(lambda: self.show_log("图像基本信息如上！"))
        self.pushButton_2.clicked.connect(lambda: self.show_log("DCT直方图已生成！"))
        self.pushButton_3.clicked.connect(lambda: self.show_log("颜色直方图已生成！"))
        self.pushButton_4.clicked.connect(lambda: self.show_log("生成式图像检测已完成！"))
        self.pushButton_5.clicked.connect(lambda: self.show_log("篡改鉴定及定位已完成！"))

        # ================== 图像处理 ==================
        self.pushButton_6.clicked.connect(lambda: self.show_log("图像还原完成！"))
        self.pushButton_7.clicked.connect(lambda: self.show_log("超分辨率完成！"))
        self.pushButton_8.clicked.connect(lambda: self.show_log("图像去模糊完成！"))
        self.pushButton_9.clicked.connect(lambda: self.show_log("图像去噪完成！"))
        self.pushButton_10.clicked.connect(lambda: self.show_log("去雨/雪/雾完成！"))

    def show_log(self, message):
        """
        槽函数：将接收到的文本显示在结果图像下方的对话框中。
        【关键】使用 setText() 而不是 append()，这样每次点击都会清空之前的内容并显示新内容。
        """
        self.txt_info.setText(message)


# ================= 运行程序的样板代码 =================
if __name__ == '__main__':
    # 固定的 PyQt 启动代码
    app = QApplication(sys.argv)
    
    # 实例化我们自己写的逻辑窗口类
    window = MyLogicWindow()
    window.show()
    
    # 进入程序主循环
    sys.exit(app.exec())