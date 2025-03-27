import sys, socket, threading, select, pyaudio
import speech_recognition as sr
from PyQt5 import QtWidgets, QtGui
from main_UI import Ui_MainWindow

class MainApp(Ui_MainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.setupUi(mainwindow)
        self.conn = None
        self.temp = ""
        
        # Load microphone list
        self.load_microphones()
        self.comboBox.currentIndexChanged.connect(self.update_selected_microphone)
        self.selected_mic_index = None  # Lưu index microphone được chọn

        # Kết nối sự kiện
        self.ConnectButton.clicked.connect(self.STM32Connect)
        self.DisconnectButton.clicked.connect(self.STM32Disconnect)
        self.OnDevice1Button.clicked.connect(lambda: self.send_data("On1"))
        self.OffDevice1Button.clicked.connect(lambda: self.send_data("Off1"))
        self.OnDevice2Button.clicked.connect(lambda: self.send_data("On2"))
        self.OffDevice2Button.clicked.connect(lambda: self.send_data("Off2"))
        self.OnDevice3Button.clicked.connect(lambda: self.send_data("On3"))
        self.OffDevice3Button.clicked.connect(lambda: self.send_data("Off3"))
        self.HoldSpeakButton.pressed.connect(self.start_speech_recognition)
    
    def STM32Connect(self):
        """Kết nối tới STM32 và yêu cầu trạng thái thiết bị"""
        self.SERVER_IP = self.lineEdit_IPAddress.text()
        self.SERVER_PORT = int(self.lineEdit_Port.text())

        try:
            self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conn.settimeout(5)
            self.conn.connect((self.SERVER_IP, self.SERVER_PORT))
            self.conn.setblocking(False)
            self.label_StatusConnection.setText("Connected")
            self.label_StatusConnection.setStyleSheet("color:rgb(133, 159, 61);")
            print(f"🟢 Kết nối thành công tới {self.SERVER_IP}:{self.SERVER_PORT}")

            # Yêu cầu STM32 gửi trạng thái thiết bị
            self.send_data("GET_STATUS")

            # Chạy luồng nhận dữ liệu
            self.receive_thread = threading.Thread(target=self.receive_data, daemon=True)
            self.receive_thread.start()

        except socket.error as e:
            self.label_StatusConnection.setText("Connection Failed")
            self.label_StatusConnection.setStyleSheet("color:rgb(204, 43, 82);")
            print(f"❌ Lỗi kết nối: {e}")
    
    def STM32Disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            self.label_StatusConnection.setText("Disconnected")
            self.label_StatusConnection.setStyleSheet("color:rgb(204, 43, 82);")
    
    def send_data(self, message):
        if self.conn and self.temp != message:
            try:
                self.conn.sendall(message.encode())
                print(f"📤 Đã gửi: {message}")
            except Exception as e:
                print(f"Failed to send data: {e}")
    
    def receive_data(self):
        """Luồng chạy nền để nhận phản hồi từ STM32 mà không chặn chương trình"""
        while self.conn:
            try:
                ready, _, _ = select.select([self.conn], [], [], 0.1)  # Chờ tối đa 100ms
                if ready:
                    data = self.conn.recv(1024).decode().strip()
                    if not data:
                        break
                    print(f"📥 Nhận phản hồi từ STM32: {data})")
                    
                    # Kiểm tra phản hồi trạng thái ban đầu
                    if len(data) == 3:  # Nhận trạng thái thiết bị
                        self.update_device_status(data)
                    else:
                        self.update_single_device(data)

            except Exception as e:
                print(f"❌ Lỗi nhận dữ liệu: {e}")
                break

    def update_device_status(self, data):
        """Cập nhật tất cả thiết bị từ phản hồi ban đầu"""
        mapping = {
            'a': lambda: self.IconDevice1.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\open.png")),
            'x': lambda: self.IconDevice1.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\close.png")),
            'b': lambda: self.IconDevice2.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\ON.png")),
            'y': lambda: self.IconDevice2.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\OFF.png")),
            'c': lambda: self.IconDevice3.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\fan on.png")),
            'z': lambda: self.IconDevice3.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\fan off.png")),
        }
        for i in range(len(data)):
            if data[i] in mapping:
                mapping[data[i]]()

    def update_single_device(self, data):
        """Cập nhật trạng thái từng thiết bị khi có thay đổi"""
        mapping = {
            'a': lambda: self.IconDevice1.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\open.png")),
            'x': lambda: self.IconDevice1.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\close.png")),
            'b': lambda: self.IconDevice2.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\ON.png")),
            'y': lambda: self.IconDevice2.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\OFF.png")),
            'c': lambda: self.IconDevice3.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\fan on.png")),
            'z': lambda: self.IconDevice3.setPixmap(QtGui.QPixmap("D:\\hocki2\\HTN-RealTime\\tieu luan\\Code\\icon\\fan off.png")),
        }
        if data in mapping:
            mapping[data]()
    
    def run_server(self):
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()

    def load_microphones(self):
        """Load danh sách microphone vào comboBox"""
        self.comboBox.clear()
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            info = p.get_device_info_by_index(i)
            self.comboBox.addItem(info["name"], i)

    def update_selected_microphone(self):
        """Cập nhật microphone được chọn từ comboBox"""
        self.selected_mic_index = self.comboBox.currentData()
        print(f"🎤 Đã chọn microphone ID: {self.selected_mic_index}")

    def get_microphone_index(self, target_name="Microphone (USB Audio Device)"):
        """Tìm đúng microphone có tên target_name"""
        p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            info = p.get_device_info_by_index(i)
            if target_name in info["name"]:  # Kiểm tra chính xác tên
                return info["index"]
        return None  # Trả về None nếu không tìm thấy
    
    def start_speech_recognition(self):
        recognizer = sr.Recognizer()
        mic_index = self.selected_mic_index

        if mic_index is None:
            print("Không tìm thấy microphone phù hợp!")
            return
        
        with sr.Microphone(device_index=mic_index) as source:
            print(f"Đang sử dụng microphone ID: {mic_index}")
            recognizer.adjust_for_ambient_noise(source)
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language="vi-VN")
                self.label_SpeechToText.setText(command)
                if "bật thiết bị 1" in command.lower():
                    self.send_data("On1")
                    print("On1_Voice")
                elif "tắt thiết bị 1" in command.lower():
                    self.send_data("Off1")
                    print("Off1_Voice")
                elif "bật thiết bị 2" in command.lower():
                    self.send_data("On2")
                    print("On2_Voice")
                elif "tắt thiết bị 2" in command.lower():
                    self.send_data("Off2")
                    print("Off2_Voice")
                elif "bật thiết bị 3" in command.lower():
                    self.send_data("On3")
                    print("On3_Voice")
                elif "tắt thiết bị 3" in command.lower():
                    self.send_data("Off3")
                    print("Off3_Voice")
                elif "bật tất cả" in command.lower():
                    self.send_data("OnAll")
                    print("OnAll_Voice")
                elif "tắt tất cả" in command.lower():
                    self.send_data("OffAll")
                    print("OffAll_Voice")
                    
            except sr.UnknownValueError:
                print("Không nhận diện được giọng nói.")
            except sr.RequestError:
                print("Không thể kết nối tới dịch vụ nhận diện.")
            except Exception as e:
                print(f"Speech Recognition Error: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    mainWin = MainApp(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
